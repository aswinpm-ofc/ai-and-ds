from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, trim, lower, upper, to_date, regexp_replace, coalesce, lit, mean, round
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType, DateType
import random

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("CustomerOrderDataCleaning") \
    .getOrCreate()

# --- Simulate messy customer order data ---
# This part is just for creating a sample DataFrame for cleaning.
# In a real scenario, you'd load from CSV, Parquet, DB, etc.

data = [
    (1, "  Alice Smith  ", "ELECTRONICS", "LAPTOP", 1200.50, "USD", 2, "2023-01-15", None, "Online", "  New York  "),
    (2, "Bob Johnson", "CLOTHING", "T-shirt", 25.00, "Usd", 5, "2023-02-20", "cash", "Store", " LA "),
    (3, "Charlie Brown", "BOOKS", "Novel", None, "USD", 1, "2023/03/05", "credit_card", "Online", "New York"), # Missing Price
    (4, "DAVID LEE", "ELECTRONICS", "Headphones", 80.00, "usd", None, "2023-04-10", "credit_card", "Online", "Chicago"), # Missing Quantity
    (5, "Eve Davis", "FOOD", "APPLE", 5.00, "USD", 10, None, "debit", "Store", "Houston"), # Missing OrderDate
    (6, "Frank White", "CLOTHING", "Jeans", 75.00, "USD", 2, "2023-05-01", "Credit_Card", "Online", " new york"), # Inconsistent 'New York'
    (7, "Grace Green", "HOME", "Lamp", 45.00, "EUR", 1, "2023-06-12", "paypal", "Online", "London"), # Different Currency
    (8, "Heidi King", "ELECTRONICS", "LAPTOP", 1200.50, "USD", 2, "2023-01-15", None, "Online", "New York"), # Duplicate of row 1 (ID, Product, Price, Qty, Date)
    (9, "Ivan Petrov", "BOOKS", "Magazine", 10.00, "USD", 3, "2023-07-01", "cash", "Store", None), # Missing City
    (10, "Julia Chen", "Food", "Orange", -5.00, "USD", 2, "2023-08-01", "debit", "Online", "San Francisco"), # Negative Price
    (11, "Kyle Baker", "CLOTHING", "Socks", 8.00, "UsD", 5, "2023-09-01", "credit_card", "Store", " LA "), # Duplicate city, inconsistent currency case
    (12, None, "HOME", "Chair", 150.00, "USD", 1, "2023-10-01", "paypal", "Online", "Miami") # Missing CustomerName
]

schema = StructType([
    StructField("OrderID", IntegerType(), False),
    StructField("CustomerName", StringType(), True),
    StructField("Category", StringType(), True),
    StructField("Product", StringType(), True),
    StructField("Price", DoubleType(), True),
    StructField("Currency", StringType(), True),
    StructField("Quantity", IntegerType(), True),
    StructField("OrderDate", StringType(), True), # Stored as String, needs conversion
    StructField("PaymentMethod", StringType(), True),
    StructField("Channel", StringType(), True),
    StructField("CustomerCity", StringType(), True)
])

df_raw = spark.createDataFrame(data, schema=schema)

print("--- Original Raw DataFrame ---")
df_raw.printSchema()
df_raw.show(truncate=False)

# --- Start Cleaning Process ---

# 1. Handle Missing Values
#    a. Impute 'CustomerName' with 'Unknown Customer'
#    b. Impute 'PaymentMethod' with 'Unknown'
#    c. Impute 'CustomerCity' with 'Unspecified'
#    d. For numerical columns 'Price' and 'Quantity', impute with the mean.

# Calculate means for Price and Quantity
mean_price = df_raw.agg(mean(col("Price"))).collect()[0][0]
mean_quantity = df_raw.agg(mean(col("Quantity"))).collect()[0][0]

print(f"\nCalculated Mean Price: {mean_price:.2f}")
print(f"Calculated Mean Quantity: {mean_quantity:.2f}")

df_cleaned = df_raw.na.fill({
    "CustomerName": "Unknown Customer",
    "PaymentMethod": "Unknown",
    "CustomerCity": "Unspecified",
    "Price": round(mean_price, 2), # Round for cleaner imputation
    "Quantity": int(round(mean_quantity, 0)) # Quantity should be integer
})

print("\n--- After Imputing Missing Values ---")
df_cleaned.show(truncate=False)


# 2. Handle Duplicates
#    Drop exact duplicate rows based on a set of key columns
#    Assuming (OrderID, Product, Price, Quantity, OrderDate) uniquely identifies an order item
df_cleaned = df_cleaned.dropDuplicates(subset=["OrderID", "Product", "Price", "Quantity", "OrderDate"])

print("\n--- After Dropping Duplicate Order Items ---")
df_cleaned.show(truncate=False)


# 3. Correct Data Types and Standardize Formats
#    a. Convert 'OrderDate' from String to DateType
#    b. Standardize string columns (trim whitespace, lowercase)

df_cleaned = df_cleaned.withColumn("OrderDate",
                                   # Try multiple date formats if necessary
                                   coalesce(to_date(col("OrderDate"), "yyyy-MM-dd"),
                                            to_date(col("OrderDate"), "yyyy/MM/dd"))
                                   ) \
    .withColumn("CustomerName", trim(col("CustomerName"))) \
    .withColumn("Category", lower(trim(col("Category")))) \
    .withColumn("Product", trim(col("Product"))) \
    .withColumn("Currency", upper(trim(col("Currency")))) \
    .withColumn("PaymentMethod", lower(regexp_replace(trim(col("PaymentMethod")), "_", ""))) \
    .withColumn("Channel", lower(trim(col("Channel")))) \
    .withColumn("CustomerCity", lower(trim(col("CustomerCity"))))

print("\n--- After Correcting Data Types and Standardizing String Formats ---")
df_cleaned.printSchema() # Check updated schema for OrderDate
df_cleaned.show(truncate=False)


# 4. Standardize Categorical Values
#    a. Standardize 'CustomerCity' (e.g., 'new york' vs 'ny', 'la' vs 'los angeles')
#    b. Standardize 'PaymentMethod' (e.g., 'creditcard' vs 'credit_card' from earlier regex)
#    c. Convert 'EUR' to 'USD' for 'Price' (assuming 1 EUR = 1.08 USD for simplicity)

df_cleaned = df_cleaned.withColumn("CustomerCity",
                                   when(col("CustomerCity") == "ny", "new york")
                                   .when(col("CustomerCity") == "la", "los angeles")
                                   .otherwise(col("CustomerCity"))
                                   ) \
    .withColumn("PaymentMethod",
                when(col("PaymentMethod") == "creditcard", "credit_card")
                .when(col("PaymentMethod") == "debit", "debit_card")
                .otherwise(col("PaymentMethod"))
                ) \
    .withColumn("Price_USD",
                when(col("Currency") == "EUR", round(col("Price") * 1.08, 2))
                .otherwise(col("Price"))
                ) \
    .drop("Price", "Currency") # Drop original price/currency if 'Price_USD' is the final desired column

print("\n--- After Standardizing Categorical Values and Currency Conversion ---")
df_cleaned.show(truncate=False)


# 5. Handle Outliers and Invalid Data
#    a. Filter out negative prices/quantities. (Assumes these are errors)
#    b. Filter out future order dates (if applicable, for historical analysis)

df_cleaned = df_cleaned.filter(col("Price_USD") >= 0) \
    .filter(col("Quantity") >= 1) \
    .filter(col("OrderDate") <= lit("2025-07-11").cast(DateType())) # Filter out future dates from current time

print("\n--- After Handling Outliers/Invalid Data (Negative Price/Quantity, Future Dates) ---")
df_cleaned.show(truncate=False)


# 6. Final Data Review
print("\n--- Final Cleaned Data Schema ---")
df_cleaned.printSchema()

print("\n--- Sample of Final Cleaned Data ---")
df_cleaned.show(truncate=False)

# Optional: Describe final DataFrame for aggregated statistics
print("\n--- Final Cleaned Data Summary Statistics ---")
df_cleaned.describe().show()

# Stop the SparkSession
spark.stop()