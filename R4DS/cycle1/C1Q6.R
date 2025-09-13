# Function to check if a number is prime
is_prime <- function(n) {
  if (n <= 1) {
    return(FALSE)
  }
  if (n == 2) {
    return(TRUE)
  }
  if (n %% 2 == 0) {
    return(FALSE)
  }
  
  for (i in 3:floor(sqrt(n))) {
    if (n %% i == 0) {
      return(FALSE)
    }
  }
  
  return(TRUE)
}

# Function to find all prime numbers in a range
find_primes_in_range <- function(start, end) {
  primes <- c()
  
  for (n in start:end) {
    if (is_prime(n)) {
      primes <- c(primes, n)
    }
  }
  
  return(primes)
}

# Main program to check a single number and find primes in a range
prime_number_checker <- function() {
  # Check if a single number is prime
  number_input <- readline(prompt = "Enter a number to check if it is prime: ")
  number <- as.integer(number_input)
  
  if (is.na(number)) {
    cat("Please enter a valid integer.\n")
    return()
  }
  
  if (is_prime(number)) {
    cat(number, "is a prime number.\n")
  } else {
    cat(number, "is not a prime number.\n")
  }
  
  # Find all primes in a specified range
  start_input <- readline(prompt = "Enter the start of the range: ")
  end_input <- readline(prompt = "Enter the end of the range: ")
  start <- as.integer(start_input)
  end <- as.integer(end_input)
  
  if (is.na(start) || is.na(end) || start > end) {
    cat("Please enter a valid range.\n")
    return()
  }
  
  primes <- find_primes_in_range(start, end)
  
  if (length(primes) > 0) {
    cat("Prime numbers between", start, "and", end, "are:\n")
    print(primes)
  } else {
    cat("There are no prime numbers in the specified range.\n")
  }
}

# Run the main program
prime_number_checker()
