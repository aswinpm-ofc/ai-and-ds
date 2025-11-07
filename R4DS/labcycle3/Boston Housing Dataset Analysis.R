library(MASS)
data(Boston)

print("First 6 rows of the Boston dataset:")
print(head(Boston))
print("Structure of the Boston dataset:")
print(str(Boston))

## a. Data Exploration and Visualization

print("Summary Statistics of Boston dataset:")
print(summary(Boston))

hist(Boston$medv, 
     main = "Histogram of Median Home Value (medv)",
     xlab = "Median Value ($1000s)",
     col = "lightblue",
     border = "black")

plot(Boston$rm, Boston$medv,
     main = "Median Value vs. Average Rooms (rm)",
     xlab = "Average number of rooms (rm)",
     ylab = "Median Value (medv)",
     pch = 19, col = "darkgreen")


## b. Regression Analysis

full_model <- lm(medv ~ ., data = Boston)
print("Summary of the Full Multiple Linear Regression Model:")
print(summary(full_model))


## c. Prediction

Boston$chas <- as.factor(Boston$chas)
full_model_factor <- lm(medv ~ ., data = Boston)

new_data <- data.frame(
  crim = mean(Boston$crim), zn = mean(Boston$zn), indus = mean(Boston$indus), 
  chas = factor(0, levels = levels(Boston$chas)), nox = mean(Boston$nox), rm = 7.0, 
  age = mean(Boston$age), dis = mean(Boston$dis), rad = mean(Boston$rad), 
  tax = mean(Boston$tax), ptratio = mean(Boston$ptratio), 
  b = mean(Boston$b), lstat = mean(Boston$lstat)
)

predicted_medv <- predict(full_model_factor, newdata = new_data)

cat("\nPrediction for a hypothetical area (rm=7.0, others at mean):\n")
cat("Predicted Median Home Value (medv) is:", round(predicted_medv, 2), "($1000s)\n")
