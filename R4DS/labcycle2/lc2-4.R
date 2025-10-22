# Extract mpg values
mpg <- mtcars$mpg

# Compute statistics
mean_mpg <- mean(mpg)
sd_mpg <- sd(mpg)

# Create histogram data (without plotting yet)
h <- hist(
  mpg,
  breaks = 8,                         # Number of bins (you can adjust)
  col = colorRampPalette(c("lightblue", "darkblue"))(8), # Shades of blue
  main = "Distribution of Miles per Gallon (mpg)",
  xlab = "Miles per Gallon",
  ylab = "Frequency",
  border = "white"
)

# Add vertical line for mean
abline(v = mean_mpg, col = "red", lwd = 2)

# Add text with mean and SD
text(
  x = mean_mpg + 2,
  y = max(h$counts) - 1,
  labels = paste0(
    "Mean = ", round(mean_mpg, 2),
    "\nSD = ", round(sd_mpg, 2)
  ),
  col = "black",
  adj = 0
)
