data(mtcars)
correlation_test <- cor.test(mtcars$hp, mtcars$mpg, method = "pearson")

print("Pearson Correlation Test Results (hp and mpg):")
print(correlation_test)

cat("\nInterpretation:\n")
cat("Correlation Coefficient (r):", round(correlation_test$estimate, 3), "\n")
cat("P-value:", format.pval(correlation_test$p.value, digits = 3), "\n")
cat("The strong negative correlation (r close to -1) suggests that as horsepower (hp) increases, miles per gallon (mpg) tends to decrease.\n")
cat("The very small p-value (typically < 0.05) indicates that this correlation is statistically significant.\n")
