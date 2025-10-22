
# Basic Exploratory Data Analysis (EDA) on Titanic Dataset


# Step 1: Load dataset
titanic <- read.csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# Step 2: Preview the data
head(titanic)
str(titanic)
summary(titanic)

# (a) Histogram: Number of Parents/Children aboard (Parch)


hist(titanic$Parch,
     main = "Number of Parents/Children Aboard (Parch)",
     xlab = "Number of Parents/Children (Parch)",
     ylab = "Number of Passengers",
     col = "lightblue",
     border = "black")


# (b) Basic EDA: Exploring Factors Influencing Survival


# Overall survival counts and rates
cat("\nOverall Survival Counts:\n")
print(table(titanic$Survived))

cat("\nOverall Survival Rate (%):\n")
print(prop.table(table(titanic$Survived)) * 100)

# Survival by Gender
cat("\nSurvival by Gender:\n")
print(table(titanic$Sex, titanic$Survived))

# Survival by Passenger Class
cat("\nSurvival by Passenger Class:\n")
print(table(titanic$Pclass, titanic$Survived))

# Average Age of Survivors vs Non-Survivors
cat("\nAverage Age by Survival Status:\n")
print(aggregate(Age ~ Survived, data = titanic, FUN = mean, na.rm = TRUE))


# (c) Boxplot: Age Distribution of Survivors vs Non-Survivors


boxplot(Age ~ Survived, data = titanic,
        main = "Age Distribution by Survival Status",
        xlab = "Survival (0 = Died, 1 = Survived)",
        ylab = "Age (years)",
        col = c("tomato", "lightgreen"),
        border = "black")

