# Load the built-in iris dataset
data(iris)

# Create a scatter plot with labels and title
png("Sepal vs petal length.png")
plot(iris$Sepal.Length, iris$Petal.Length,
     main = "Scatterplot of Sepal Length vs Petal Length",
     xlab = "Sepal Length (cm)",
     ylab = "Petal Length (cm)",
     col = "blue",
     pch = 19)  # solid circle points
       

# Close the device to save the file
dev.off()
