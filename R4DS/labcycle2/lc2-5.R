# Extract variables
hp <- mtcars$hp
gear <- as.factor(mtcars$gear)  # Gears as factor

# Create boxplot
boxplot(
  hp,
  main = "Boxplot of Horsepower (hp)",
  ylab = "Horsepower",
  xlab = "",
  outline = TRUE,
  col = "lightblue"
)

# Identify outliers
bp <- boxplot.stats(hp)
outliers <- bp$out
outlier_indices <- which(hp %in% outliers)

# Add points with shapes based on gear
points(
  rep(1, length(hp)),            # x-coordinate (all at 1)
  hp,
  pch = as.numeric(gear) + 15,   # Different shapes for gear
  col = "darkblue"
)

# Add legend for gear
legend(
  "topright",
  legend = levels(gear),
  pch = as.numeric(levels(gear)) + 15,
  col = "darkblue",
  title = "Number of Gears"
)

# Label outliers
text(
  x = rep(1.05, length(outliers)),
  y = outliers,
  labels = rownames(mtcars)[outlier_indices],
  col = "red",
  cex = 0.8,
  pos = 4
)
