library(forecast)
data_url <- "https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv"
covid_data <- read.csv(data_url)
covid_india <- subset(covid_data, Country.Region == "India")
covid_india$Date <- as.Date(covid_india$Date)
start_date <- as.Date("2020-01-22")
end_date <- as.Date("2020-12-15")
covid_subset <- subset(covid_india, Date >= start_date & Date <= end_date)

covid_subset$New_Confirmed <- c(0, diff(covid_subset$Confirmed))
covid_subset$New_Deaths <- c(0, diff(covid_subset$Deaths))
covid_subset$Week <- format(covid_subset$Date, "%Y-%W")

weekly_data <- aggregate(cbind(New_Confirmed, New_Deaths) ~ Week, 
                         data = covid_subset, 
                         sum, na.rm = TRUE)
weekly_data <- weekly_data[order(weekly_data$Week), ]
weekly_data <- weekly_data[-1,]

## a) Univariate Time Series Analysis:

cases_ts <- ts(weekly_data$New_Confirmed, start = c(2020, 4), frequency = 52) 
print("Univariate Time Series Object (Weekly New Cases):")
print(cases_ts)

plot(cases_ts, 
     main = "Weekly New COVID-19 Cases in India (Time Series)", 
     xlab = "Time (Week)", 
     ylab = "New Cases",
     col = "blue", 
     lwd = 2)


## b) Multivariate Time Series Analysis:

deaths_ts <- ts(weekly_data$New_Deaths, start = c(2020, 4), frequency = 52)
multi_ts <- cbind(cases_ts, deaths_ts)
colnames(multi_ts) <- c("Cases", "Deaths")
print("Multivariate Time Series Object:")
print(multi_ts)

ts.plot(multi_ts, 
        gpars = list(col = c("blue", "red"), lwd = 2), 
        main = "Weekly New Cases (Blue) and Deaths (Red) in India",
        xlab = "Time (Week)",
        ylab = "Count")
legend("topleft", 
       legend = c("Cases", "Deaths"), 
       col = c("blue", "red"), 
       lty = 1, 
       cex = 0.8)


## c) Time Series Forecasting:

arima_model <- auto.arima(cases_ts)
print("Fitted ARIMA Model for New Cases (auto.arima):")
print(arima_model)

forecast_values <- forecast(arima_model, h = 5)
print("Forecasted Next 5 Weeks:")
print(forecast_values)

plot(forecast_values, 
     main = "ARIMA Forecast of Weekly New COVID-19 Cases",
     xlab = "Time (Week)",
     ylab = "New Cases")
