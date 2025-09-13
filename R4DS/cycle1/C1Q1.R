# Function to perform the tasks
process_text <- function(text, word_to_replace, replacement_word) {
  # Split text into words
  words <- unlist(strsplit(text, "\\s+"))
  
  # Debugging print
  print(words)
  
  # a. Count the total number of words
  total_words <- length(words)
  cat("Total number of words:", total_words, "\n")
  
  # b. Calculate the average word length
  word_lengths <- nchar(words)
  average_word_length <- mean(word_lengths)
  cat("Average word length:", average_word_length, "\n")
  
  # c. Identify and print the longest word
  longest_word <- words[which.max(word_lengths)]
  cat("Longest word:", longest_word, "\n")
  
  # d. Replace all occurrences of a specific word with another word of your choice
  replaced_text <- gsub(word_to_replace, replacement_word, text)
  cat("Modified text:", replaced_text, "\n")
}

# Accept input from the user
paragraph <- readline(prompt = "Enter a paragraph of text: ")
word_to_replace <- readline(prompt = "Enter the word to be replaced: ")
replacement_word <- readline(prompt = "Enter the replacement word: ")

# Print inputs for debugging
cat("Input paragraph:", paragraph, "\n")
cat("Word to replace:", word_to_replace, "\n")
cat("Replacement word:", replacement_word, "\n")

# Process the input text
process_text(paragraph, word_to_replace, replacement_word)

