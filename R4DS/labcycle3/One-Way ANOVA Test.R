data(mtcars)
mtcars$gear_factor <- as.factor(mtcars$gear)
anova_model <- aov(disp ~ gear_factor, data = mtcars)

print("One-Way ANOVA Test Results (Displacement across Gear Types):")
anova_summary <- summary(anova_model)
print(anova_summary)

p_value <- anova_summary[[1]]$`Pr(>F)`[1]
cat("\nInterpretation:\n")
cat("P-value for the ANOVA test:", format.pval(p_value, digits = 3), "\n")

if (p_value < 0.05) {
  cat("Since the p-value is less than 0.05, we reject the null hypothesis.\n")
  cat("There is a **statistically significant** variation in the average displacement (disp) across the different gear types (gear).\n")
} else {
  cat("Since the p-value is not less than 0.05, we do not reject the null hypothesis.\n")
  cat("There is **no statistically significant** variation in the average displacement (disp) across the different gear types (gear).\n")
}
