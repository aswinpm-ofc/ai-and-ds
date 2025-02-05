import numpy as np


def gaussian_elimination(A, b):
    
    
    
    
    n = len(A)
    
    
    augmented_matrix = np.hstack([A, b.reshape(-1, 1)])

   
    for i in range(n):
        
       
       
        max_row = np.argmax(np.abs(augmented_matrix[i:n, i])) + i
        
        
        augmented_matrix[[i, max_row]] = augmented_matrix[[max_row, i]]
        

        for j in range(i+1, n):
            
            if augmented_matrix[j, i] != 0:
                factor = augmented_matrix[j, i] / augmented_matrix[i, i]
                
                augmented_matrix[j, i:] -= factor * augmented_matrix[i, i:]
                
                


    x = np.zeros(n)
    
    for i in range(n-1, -1, -1):
        
        
        
        
        x[i] = (augmented_matrix[i, -1] - np.dot(augmented_matrix[i, i+1:n], x[i+1:])) / augmented_matrix[i, i]

    return x



def gauss_seidel(A, b, max_iterations=100, tolerance=1e-10):
    
    
    n = len(A)
    x = np.zeros_like(b)
    

    for it in range(max_iterations):
        
        
        
        
        
        
        
        
        
        
        
        
        x_new = np.copy(x)
        

        for i in range(n):
            
            
            sum_ = np.dot(A[i, :], x_new) - A[i, i] * x_new[i]
            
            x_new[i] = (b[i] - sum_) / A[i, i]
            

   
        if np.linalg.norm(x_new - x, ord=np.inf) < tolerance:
            
            return x_new


        x = x_new
        

    return x



def get_input_matrix():
    
    
    
    n = int(input("Enter the number of equations (size of the matrix): "))
    
    A = []
    b = []

    print(f"\nEnter the coefficients for each of the {n} equations:")
    for i in range(n):
        row = list(map(float, input(f"Enter the coefficients of equation {i+1} separated by spaces: ").split()))
        
        
        
        
        A.append(row)
        
        
        constant = float(input(f"Enter the constant term for equation {i+1}: "))
        
        
        b.append(constant)

    return np.array(A), np.array(b)


def main():
    print("\nWelcome to the Linear Equation Solver!\n")

    A, b = get_input_matrix()

    print("\nChoose the method to solve the system of equations:")
    
    
    print("1. Gaussian Elimination")
    
    
    
    print("2. Gauss-Seidel")
    

   
    method = input("Enter 1 for Gaussian Elimination or 2 for Gauss-Seidel: ").strip()

    if method == '1':
        
        
        print("\nSolving using Gaussian Elimination...\n")
        
        try:
            
            solution = gaussian_elimination(A, b)
            
            print("The solution to the system is:")
            
            
            for i in range(len(solution)):
                
                
                
                print(f"x{i+1} = {solution[i]:.6f}")
                
                
        except Exception as e:
            
            
            print(f"\nError during Gaussian Elimination: {e}")
    
    elif method == '2':
        
        
        
        print("\nSolving using Gauss-Seidel...\n")
        
        
        solution = gauss_seidel(A, b)
        
        
        print("The solution to the system is:")
        
        
        for i in range(len(solution)):
            
            
            
            print(f"x{i+1} = {solution[i]:.6f}")
            
            
    
    else:
        
        
        
        print("\nInvalid choice! Please enter 1 for Gaussian Elimination or 2 for Gauss-Seidel.")




if __name__ == "__main__":
    
    main()
