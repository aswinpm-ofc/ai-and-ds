# Function to generate a random password
generate_password <- function(length) {
  if (!is.numeric(length) || length <= 0 || length != as.integer(length)) {
    stop("Password length must be a positive integer.")
  }
  
  # Define character sets
  lowercase <- letters
  uppercase <- toupper(letters)
  digits <- 0:9
  special_chars <- c("!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "<", ">", ".", "?", "/")
  
  # Combine all character sets
  all_chars <- c(lowercase, uppercase, digits, special_chars)
  
  # Randomly sample characters to create the password
  password <- sample(all_chars, length, replace = TRUE)
  
  # Ensure the password includes at least one of each character set
  password <- c(
    sample(lowercase, 1),
    sample(uppercase, 1),
    sample(digits, 1),
    sample(special_chars, 1),
    sample(all_chars, length - 4, replace = TRUE)
  )
  
  # Shuffle the password to mix characters
  password <- sample(password, length)
  
  # Convert to a single string
  password <- paste(password, collapse = "")
  
  return(password)
}

# Main program
length_input <- readline(prompt = "Enter the desired password length: ")
length <- as.integer(length_input)

if (length < 4) {
  cat("Password length must be at least 4 characters.\n")
} else {
  password <- generate_password(length)
  cat("Generated password:", password, "\n")
}
