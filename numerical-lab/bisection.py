import sympy as sp
def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        print("Function does not change signs in the interval. Bisection method cannot be applied.")
        return None
    
    iter_count = 0
    while (b - a) / 2 > tol and iter_count < max_iter:
        c = (a + b) / 2
        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iter_count += 1
    
    
    root = (a + b) / 2
    return root


def get_function_input():
    func_input = input("Enter a function in terms of x (e.g., 'x**2 - 4'): ")
    x = sp.symbols('x')
    func_expr = sp.sympify(func_input)  
    f = sp.lambdify(x, func_expr, 'numpy')  
    return f

def main():
    print("Welcome to the Bisection Method!")
    
 
    choice = input("Do you want to enter your own function (yes/no)? ").lower()
    
    if choice == 'yes':
        f = get_function_input()
    else:
       
        print("Using default function: f(x) = x^2 - 4")
        def f(x):
            return x**2 - 4
    

    a = float(input("Enter the starting point a: "))
    b = float(input("Enter the ending point b: "))
    tol = float(input("Enter the tolerance (default 1e-6): ") or 1e-6)
    
    
    root = bisection_method(f, a, b, tol)
    
    if root is not None:
        print(f"The root is approximately: {root}")
    else:
        print("Root could not be found.")
    
if __name__ == "__main__":
    main()
