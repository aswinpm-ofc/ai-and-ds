# Load the built-in dataset
data(iris)

# View the structure of the dataset
str(iris)

# Summary statistics
summary(iris)

# Check the first few rows
head(iris)
# Check for missing data
colSums(is.na(iris))
# Boxplot of Sepal.Length across species
boxplot(Sepal.Length ~ Species, data = iris,
        main = "Sepal Length by Species",
        xlab = "Species",
        ylab = "Sepal Length (cm)",
        col = c("lightblue", "lightgreen", "lightpink"))
# One-way ANOVA test
anova_result <- aov(Sepal.Length ~ Species, data = iris)
summary(anova_result)
pairs(iris[1:4],
      main = "Pair Plot of Iris Features",
      pch = 19,
      col = iris$Species)
