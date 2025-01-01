
a = int(input("Enter the number of rows for Matrix 1: "))
b = int(input("Enter the number of columns for Matrix 1: "))

c = int(input("Enter the number of rows for Matrix 2: "))
d = int(input("Enter the number of columns for Matrix 2: "))

# Validate that the matrices can be added
if a != c or b != d:
    print("Error: Matrices must have the same dimensions to be added.")
    exit()

# Initialize matrices
matrix1 = [[0 for _ in range(b)] for _ in range(a)]
matrix2 = [[0 for _ in range(d)] for _ in range(c)]

# Input values for Matrix 1
print("Enter the values for Matrix 1:")
for i in range(a):
    for j in range(b):
        matrix1[i][j] = int(input(f"Matrix 1[{i}][{j}]: "))

# Input values for Matrix 2
print("Enter the values for Matrix 2:")
for i in range(c):
    for j in range(d):
        matrix2[i][j] = 
        int(input(f"Matrix 2[{i}][{j}]: "))

# Function to add matrices
def sub_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    matrix3 = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            matrix3[i][j] = matrix1[i][j] - matrix2[i][j]
    return matrix3

# Add the matrices
result_matrix = sub_matrices(matrix1, matrix2)

# Print the resulting matrix
print("The resulting matrix after addition is:")
for row in result_matrix:
    print(row)
