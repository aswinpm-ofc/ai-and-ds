library(ggplot2)
set.seed(42)
house_data <- data.frame(
  GrLivArea = 1000 + (1:50) * 50 + rnorm(50, 0, 100),
  SalePrice = 100000 + (1:50) * 5000 + rnorm(50, 0, 50000)
)
colnames(house_data) <- c("size", "price")

model <- lm(price ~ size, data = house_data)

coefficients <- coef(model)
print("Regression Coefficients (Intercept and Slope):")
print(coefficients)

plot_model <- ggplot(house_data, aes(x = size, y = price)) +
  geom_point(color = 'blue') +
  geom_smooth(method = "lm", col = "red") +
  labs(title = "House Price vs. Size with Regression Line",
       x = "House Size (sq. ft.)",
       y = "House Price") +
  theme_minimal()

print(plot_model)

intercept <- coefficients[1]
slope <- coefficients[2]
print(paste("Intercept:", round(intercept, 2)))
print(paste("Slope:", round(slope, 2)))
