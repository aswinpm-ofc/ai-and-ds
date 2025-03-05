import sympy as sp
from mpmath import mp

# Function to accept user input and compute the derivative using Central Difference Method (CDM)
def central_difference_method():
    # Set the precision level in mpmath (more digits for accuracy)
    mp.dps = 50  # Set decimal places to 50 for higher precision

    # Accept user input for the function
    user_function = input("Enter the function (in terms of x): ")
    
    # Define the symbol for x using sympy
    x = sp.symbols('x')
    
    # Convert the user input to a sympy expression
    f = sp.sympify(user_function)

    # Ask the user for the point where they want the derivative (using sympify to handle symbolic inputs)
    point = sp.sympify(input("Enter the point where you want the derivative: "))
    
    # Ask for the step size
    h = float(input("Enter the step size (h): "))
    
    # Central Difference Formula for first derivative
    f_plus_h = f.subs(x, point + h)   # f(x + h)
    f_minus_h = f.subs(x, point - h)  # f(x - h)
    
    # Estimate the derivative using the Central Difference Method
    central_difference_derivative = (f_plus_h - f_minus_h) / (2 * h)
    
    # Use sympy's N() function to evaluate with floating point precision
    result = sp.N(central_difference_derivative, 50)  # This ensures you get the result with higher precision
    
    # Print the result with a high number of decimal places
    print(f"Estimated derivative of the function at x = {point} using Central Difference Method is: {result:.10f}")

# Call the function
central_difference_method()
