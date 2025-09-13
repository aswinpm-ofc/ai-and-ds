# Function to generate the Fibonacci series with a twist
generate_twisted_fibonacci <- function(n_terms) {
  if (n_terms < 1) {
    return(cat("Please enter a positive integer greater than 0.\n"))
  }
  
  # Initialize the first three terms
  series <- c(0, 1, 1)
  
  # Generate the series
  for (i in 4:n_terms) {
    next_term <- sum(series[(i-3):(i-1)])
    series <- c(series, next_term)
  }
  
  return(series[1:n_terms])
}

# Main program
n_terms_input <- readline(prompt = "Enter the number of terms: ")
n_terms <- as.integer(n_terms_input)

if (is.na(n_terms) || n_terms <= 0) {
  cat("Please enter a valid positive integer.\n")
} else {
  twisted_fibonacci_series <- generate_twisted_fibonacci(n_terms)
  cat("Twisted Fibonacci Series:\n")
  print(twisted_fibonacci_series)
}
