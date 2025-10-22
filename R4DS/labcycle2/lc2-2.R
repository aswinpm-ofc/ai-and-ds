
mtcars$cyl <- as.factor(mtcars$cyl)

colors <- c("purple", "green", "orange")

plot(mpg ~ disp, data = mtcars,
     main = "Scatterplot of MPG vs. Displacement",
     xlab = "Displacement (cu.in.)",
     ylab = "Miles per Gallon (MPG)",
     col = colors[mtcars$cyl],
     pch = 19)

for (level in levels(mtcars$cyl)) {

  subset_data <- subset(mtcars, cyl == level)


  lines(lowess(subset_data$disp, subset_data$mpg),
        col = colors[which(levels(mtcars$cyl) == level)],
        lwd = 2)
}

legend("topright",
       legend = levels(mtcars$cyl),
       title = "Number of Cylinders",
       col = colors,
       pch = 19,
       bty = "y")
