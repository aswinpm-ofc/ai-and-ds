import sympy as sp
from mpmath import mp


def central_difference_method():
    mp.dps = 50 
    user_function = input("Enter the function (in terms of x): ")
    x = sp.symbols('x')
    f = sp.sympify(user_function)
    point = sp.sympify(input("Enter the point where you want the derivative: "))
    h = float(input("Enter the step size (h): "))
    f_plus_h = f.subs(x, point + h) 
    f_minus_h = f.subs(x, point - h)  
    central_difference_derivative = (f_plus_h - f_minus_h) / (2 * h)
    
    result = sp.N(central_difference_derivative, 50) 
    
    print(f"Estimated derivative of the function at x = {point} using Central Difference Method is: {result:.10f}")


central_difference_method()
