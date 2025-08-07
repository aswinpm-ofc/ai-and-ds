
my_vector <- c(1, 5, 8, 12, 15)

my_strings <- c("apple", "banana", "cherry")


my_vector[2] 


my_vector[2:4] 


my_vector[3] <- 100


my_array <- array(1:24, dim = c(2, 3, 4))

my_array[1, 2, 3] 



my_data_frame <- data.frame(
  name = c("Alice", "Bob", "Charlie"),
  age = c(25, 30, 35),
  is_student = c(TRUE, FALSE, TRUE)
)
my_data_frame$age 


my_data_frame[, "name"] 

my_data_frame[2, 3] 



# Create a vector of numbers from 1 to 10
my_numbers <- 1:10

# Access elements based on a condition
even_numbers <- my_numbers[my_numbers %% 2 == 0]

# Perform a simple calculation on the entire vector
doubled_numbers <- my_numbers * 2



# Create a 2x3 matrix by binding columns
m1 <- cbind(c(1, 2), c(3, 4), c(5, 6))

# Create a matrix by binding rows
m2 <- rbind(c(10, 20), c(30, 40))

# Multiply two matrices (requires compatible dimensions)
matrix_product <- m2 %*% matrix(c(1,2,3,4), nrow=2, byrow=TRUE)


# Create a simple data frame for demonstration
df <- data.frame(id = 1:3, name = c("A", "B", "C"), value = c(100, 200, 150))

# Filter the data frame to show only rows where 'value' is greater than 150
filtered_df <- df[df$value > 150, ]

# Add a new column to the data frame
df$is_high_value <- df$value > 150