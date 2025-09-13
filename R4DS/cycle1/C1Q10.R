# Function to reverse a list using recursion
reverse_list <- function(lst) {
  # Base case: if the list is empty or has one element, return it as is
  if (length(lst) == 0 || length(lst) == 1) {
    return(lst)
  }
  
  # Recursive case: concatenate the last element with the reversed remainder of the list
  return(c(lst[length(lst)], reverse_list(lst[-length(lst)])))
}

# Main program
input_list <- as.list(strsplit(readline(prompt = "Enter elements of the list separated by space: "), " ")[[1]])

reversed_list <- reverse_list(input_list)

cat("Reversed list:\n")
print(reversed_list)
