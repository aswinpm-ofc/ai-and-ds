# Function to perform run-length encoding
run_length_encoding <- function(input_string) {
  # Initialize variables
  compressed_string <- ""
  n <- nchar(input_string)
  
  # Edge case for empty string
  if (n == 0) {
    return(compressed_string)
  }
  
  # Convert string to a character vector
  char_vector <- strsplit(input_string, NULL)[[1]]
  
  # Initialize the first character
  current_char <- char_vector[1]
  count <- 1
  
  # Iterate over the string
  for (i in 2:n) {
    if (char_vector[i] == current_char) {
      # Increment count if the character is the same
      count <- count + 1
    } else {
      # Append the current character and count to the compressed string
      compressed_string <- paste0(compressed_string, current_char, count)
      
      # Update the current character and reset the count
      current_char <- char_vector[i]
      count <- 1
    }
  }
  
  # Append the last character and count
  compressed_string <- paste0(compressed_string, current_char, count)
  
  return(compressed_string)
}

# Main program
input_string <- readline(prompt = "Enter a string to compress using run-length encoding: ")

compressed_string <- run_length_encoding(input_string)

cat("Compressed string:", compressed_string, "\n")
