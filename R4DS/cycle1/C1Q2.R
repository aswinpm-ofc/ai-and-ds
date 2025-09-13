# Function to encrypt a character using Caesar cipher
encrypt_char <- function(char, shift) {
  if (grepl("[A-Za-z]", char)) {
    ascii <- as.numeric(charToRaw(char))
    if (char %in% LETTERS) {
      # Uppercase letters
      ascii_shifted <- ((ascii - 65 + shift) %% 26) + 65
    } else {
      # Lowercase letters
      ascii_shifted <- ((ascii - 97 + shift) %% 26) + 97
    }
    return(rawToChar(as.raw(ascii_shifted)))
  } else {
    return(char)
  }
}

# Function to encrypt a sentence using Caesar cipher
encrypt_sentence <- function(sentence, shift) {
  encrypted_sentence <- sapply(strsplit(sentence, NULL)[[1]], encrypt_char, shift)
  return(paste(encrypted_sentence, collapse = ""))
}

# Accept input from the user
sentence <- readline(prompt = "Enter a sentence to encrypt: ")
shift <- as.integer(readline(prompt = "Enter the shift value: "))

# Encrypt the sentence
encrypted_sentence <- encrypt_sentence(sentence, shift)

# Print the encrypted sentence
cat("Encrypted sentence:", encrypted_sentence, "\n")
