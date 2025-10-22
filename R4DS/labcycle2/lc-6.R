# Load data
data(mtcars)

# Define colors and sizes based on number of carburetors
carb_colors <- rainbow(length(unique(mtcars$carb)))[as.factor(mtcars$carb)]
carb_sizes <- mtcars$carb * 1.5  # Scale sizes

# Create scatter plot
plot(mtcars$wt, mtcars$disp,
     main = "Scatter Plot of Displacement vs Weight",
     xlab = "Weight (1000 lbs)",
     ylab = "Displacement (cu.in.)",
     col = carb_colors,
     pch = 19,
     cex = carb_sizes / 5)  # adjust size scaling

# Add smooth line (trend)
lines(lowess(mtcars$wt, mtcars$disp), col = "black", lwd = 2)

# Add legend
legend("topleft",
       legend = paste("Carburetors =", sort(unique(mtcars$carb))),
       col = rainbow(length(unique(mtcars$carb))),
       pch = 19,
       title = "Number of Carburetors")
