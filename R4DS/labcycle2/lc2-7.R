# Install the necessary packages for data and time series analysis
install.packages("COVID19")
install.packages("forecast")

# Load required packages
library(ggplot2)
library(dplyr)
library(lubridate)
library(tidyr)

# --------------------------------------------
# 1. Read the data from the GitHub raw URL
# --------------------------------------------
url <- "https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv"
covid <- read.csv(url, stringsAsFactors = FALSE)

# Preview
head(covid)
str(covid)

# --------------------------------------------
# 2. Clean / transform
# --------------------------------------------

# Convert date column to Date type
covid$Date <- as.Date(covid$Date)

# Sometimes there’s more than one row per country per date (if region data)
# Aggregate globally (sum over all countries) for each date
covid_global <- covid %>%
  group_by(Date) %>%
  summarise(
    Confirmed = sum(Confirmed, na.rm = TRUE),
    Deaths = sum(Deaths, na.rm = TRUE),
    Recovered = sum(Recovered, na.rm = TRUE)
  ) %>%
  arrange(Date)

# Alternatively, if you want to plot for a specific country (e.g. “India”):
covid_country <- covid %>%
  filter(Country.Region == "India") %>%
  group_by(Date) %>%
  summarise(
    Confirmed = sum(Confirmed, na.rm = TRUE),
    Deaths = sum(Deaths, na.rm = TRUE),
    Recovered = sum(Recovered, na.rm = TRUE)
  ) %>%
  arrange(Date)


# 3. Plot time series of Confirmed cases (global)


p <- ggplot(covid_global, aes(x = Date, y = Confirmed)) +
  geom_line(color = "steelblue", size = 1) +
  geom_point(color = "darkblue", size = 1.5) +
  labs(
    title = "Global COVID-19 Confirmed Cases Over Time",
    x = "Date",
    y = "Cumulative Confirmed Cases"
  ) +
  theme_minimal()

print(p)


# 4. Plot multiple metrics together (Confirmed, Deaths, Recovered)


# Pivot to long form
covid_long <- covid_global %>%
  pivot_longer(cols = c("Confirmed", "Deaths", "Recovered"),
               names_to = "Metric",
               values_to = "Count")

p2 <- ggplot(covid_long, aes(x = Date, y = Count, color = Metric)) +
  geom_line(size = 1) +
  labs(
    title = "COVID-19 Global Trends: Confirmed, Deaths, Recovered",
    x = "Date",
    y = "Count",
    color = "Metric"
  ) +
  theme_minimal()

print(p2)


# 5. (Optional) Plot for specific country

p_india <- ggplot(covid_country, aes(x = Date, y = Confirmed)) +
  geom_line(color = "forestgreen") +
  labs(
    title = "COVID-19 Confirmed Cases Over Time in India",
    x = "Date",
    y = "Cumulative Confirmed Cases"
  ) +
  theme_minimal()

print(p_india)

# --------------------------------------------
# End of script
# --------------------------------------------
