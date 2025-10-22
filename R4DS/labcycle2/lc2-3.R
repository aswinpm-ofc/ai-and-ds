# Convert variables to factors
x <- as.factor(mtcars$cyl)   # Cylinders
y <- as.factor(mtcars$am)    # Transmission type (0 = Auto, 1 = Manual)

# Create a frequency table
tbl <- table(x, y)


# Create the bar plot
barplot(
  t(tbl),
  beside = TRUE,                             # Side-by-side bars for each transmission
  col = c("steelblue", "orange"),            # Colors for transmission types
  main = "Number of Cars by Cylinders and Transmission Type",
  xlab = "Number of Cylinders",
  ylab = "Count of Cars",
  legend.text = c("Automatic", "Manual"),    # Legend labels
  args.legend = list(title = "Transmission", x = "topright")
)
