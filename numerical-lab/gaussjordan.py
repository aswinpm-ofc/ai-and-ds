import numpy as np

def gauss_jordan(a, b):
    
    n = len(b)
    
    aug_matrix = np.hstack((a, b.reshape(-1, 1)))
    

    for i in range(n):
        
       
        diag_element = aug_matrix[i, i]
        
        aug_matrix[i] = aug_matrix[i] / diag_element
        

        for j in range(n):
            
            if i != j:
                
                
                factor = aug_matrix[j, i]
                
                
                aug_matrix[j] -= factor * aug_matrix[i]
                
                
                

    return aug_matrix[:, -1]  



n = int(input("Enter the number of equations: "))



A = []
print("Enter the coefficients row by row:")





for i in range(n):
    
    
    
    
    
    row = list(map(float, input(f"Row {i+1}: ").split()))
    
    
    
    
    A.append(row)


B = list(map(float, input("Enter the constant terms: ").split()))


A = np.array(A, dtype=float)

B = np.array(B, dtype=float)


solution = gauss_jordan(A, B)



print("Solution:")


for i in range(n):
    
    
    
    print(f"x{i+1} = {solution[i]}")
