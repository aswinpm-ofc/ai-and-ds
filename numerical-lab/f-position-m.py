import sympy as sp

def false_position():
    
    print("Enter the function f(x):")
    expr = input("f(x) = ")
    x = sp.symbols('x')
    f = sp.sympify(expr)
    a = float(input("Enter the lower bound a: "))
    b = float(input("Enter the upper bound b: "))

    
    if f.subs(x, a) * f.subs(x, b) >= 0:
        print("The function does not change sign on the interval [a, b].")
        print("Please choose a valid interval.")
        return
    tol = float(input("Enter the tolerance (e.g., 1e-6): "))
    max_iter = int(input("Enter the maximum number of iterations: "))
    print("\nIteration\ta\tb\tc\tf(c)")

    for iteration in range(1, max_iter + 1):
        fa = f.subs(x, a)
        fb = f.subs(x, b)
        c = b - (fb * (b - a)) / (fb - fa)
        fc = f.subs(x, c)
        print(f"{iteration}\t{a:.6f}\t{b:.6f}\t{c:.6f}\t{fc:.6e}")

        
        if abs(fc) < tol:
            print(f"\nThe root is approximately c = {c:.6f} (found within tolerance).")
            return
        if fa * fc < 0:
            b = c
        else:
            a = c

    print(f"\nThe method did not converge within {max_iter} iterations.")
    print(f"The last approximation is c = {c:.6f}")


false_position()
