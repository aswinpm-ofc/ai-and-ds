# Function to validate age
validate_age <- function(age) {
  return(!is.na(age) && age > 0 && age == as.integer(age))
}

# Function to validate grade
validate_grade <- function(grade) {
  return(grade %in% c("A", "B", "C", "D", "F"))
}

# Function to read student records and perform validations
read_student_records <- function() {
  student_names <- c()
  student_ages <- c()
  student_grades <- c()
  
  while(TRUE) {
    name <- readline(prompt = "Enter student name (or type 'done' to finish): ")
    name <- trimws(tolower(name))
    
    # Debugging print
    cat("Entered name:", name, "\n")
    
    if (name == "done") {
      break
    }
    
    age_input <- readline(prompt = "Enter student age: ")
    age <- as.integer(age_input)
    
    # Debugging print
    cat("Entered age:", age, "\n")
    
    if (!validate_age(age)) {
      cat("Invalid age. Please enter a positive integer.\n")
      next
    }
    
    grade <- readline(prompt = "Enter student grade (A, B, C, D, F): ")
    grade <- trimws(toupper(grade))
    
    # Debugging print
    cat("Entered grade:", grade, "\n")
    
    if (!validate_grade(grade)) {
      cat("Invalid grade. Please enter a valid letter grade (A, B, C, D, F).\n")
      next
    }
    
    student_names <- c(student_names, name)
    student_ages <- c(student_ages, age)
    student_grades <- c(student_grades, grade)
  }
  
  data.frame(Name = student_names, Age = student_ages, Grade = student_grades)
}

# Function to calculate and display average age of students with valid records
calculate_average_age <- function(student_records) {
  if (nrow(student_records) == 0) {
    cat("No valid student records available.\n")
    return(NULL)
  }
  
  average_age <- mean(student_records$Age)
  cat("Average age of students with valid records:", average_age, "\n")
}

# Main program
student_records <- read_student_records()
print(student_records)
calculate_average_age(student_records)
