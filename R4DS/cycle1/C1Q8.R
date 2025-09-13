# Function to check if a string is a palindrome
is_palindrome <- function(input_string) {
  # Remove spaces, punctuation, and convert to lowercase
  cleaned_string <- tolower(gsub("[^a-zA-Z0-9]", "", input_string))
  
  # Reverse the cleaned string
  reversed_string <- paste(rev(strsplit(cleaned_string, NULL)[[1]]), collapse = "")
  
  # Check if the cleaned string is the same forwards and backwards
  return(cleaned_string == reversed_string)
}

# Main program
input_string <- readline(prompt = "Enter a string to check if it's a palindrome: ")

if (is_palindrome(input_string)) {
  cat("The string is a palindrome.\n")
} else {
  cat("The string is not a palindrome.\n")
}
