import sympy as sp
from mpmath import mp
def central_difference_derivative():
    mp.dps = 50 
    user_function = input("Enter the function (in terms of x): ")
    x = sp.symbols('x')
    f = sp.sympify(user_function)
    point = sp.sympify(input("Enter the point where you want the derivative: "))
    h = float(input("Enter the step size (h): "))
    derivative_type = input("Which derivative do you want? Type 'first' for first derivative or 'second' for second derivative: ").lower()
    if derivative_type == 'first':
        f_plus_h = f.subs(x, point + h)   
        f_minus_h = f.subs(x, point - h) 
        first_derivative = (f_plus_h - f_minus_h) / (2 * h)
        result = sp.N(first_derivative, 50)
        print(f"Estimated first derivative of the function at x = {point} using Central Difference Method is: {result:.10f}")
    elif derivative_type == 'second':
        f_plus_h = f.subs(x, point + h)  
        f_minus_h = f.subs(x, point - h)  
        f_at_point = f.subs(x, point)    
        second_derivative = (f_plus_h - 2*f_at_point + f_minus_h) / (h**2)
        result = sp.N(second_derivative, 50) 
        print(f"Estimated second derivative of the function at x = {point} using Central Difference Method is: {result:.10f}")
    else:
        print("Invalid input. Please type 'first' or 'second' to choose the derivative type.")

central_difference_derivative()
