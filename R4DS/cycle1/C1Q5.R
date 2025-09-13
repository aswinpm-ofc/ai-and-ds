# Function to calculate the sum of the series
calculate_series_sum <- function(n_terms) {
  sum <- 0
  sign <- 1
  
  for (i in 1:n_terms) {
    numerator <- i
    denominator <- 2 * i - 1
    term <- sign * (numerator / denominator)
    sum <- sum + term
    sign <- -sign  # Alternate the sign for the next term
  }
  
  return(sum)
}

# Main program
n_terms_input <- readline(prompt = "Enter the number of terms in the series: ")
n_terms <- as.integer(n_terms_input)

if (is.na(n_terms) || n_terms <= 0) {
  cat("Please enter a positive integer for the number of terms.\n")
} else {
  series_sum <- calculate_series_sum(n_terms)
  cat("The sum of the series up to", n_terms, "terms is:", series_sum, "\n")
}
