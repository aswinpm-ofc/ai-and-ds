# ddh_check_interactive.py

def get_integer_input(prompt):
    """Helper function to safely get integer input."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Invalid input. Please enter a valid integer.")

def check_ddh_problem_interactive():
    """
    Computes g^(x*y) mod p with user input and checks against potential secrets (h).
    """
    print("\n--- Decisional Diffie-Hellman Problem Solver ---")
    
    # 1. Get Public Parameters
    print("\n[Input 1: PRIME MODULUS (P)]")
    print("P = 12347 is used in the problem, but you can enter a different prime.")
    p = get_integer_input("Enter the prime modulus (P, e.g., 12347): ")
    
    print("\n[Input 2: GENERATOR (G)]")
    print("G = 2 is the primitive root used in the problem.")
    g = get_integer_input("Enter the generator (G, e.g., 2): ")

    # 2. Get Exponents (x and y)
    print("\n[Input 3 & 4: EXPONENTS (X and Y)]")
    print("X and Y are the Discrete Logarithms, meaning 2^X ≡ 8938 and 2^Y ≡ 9620.")
    print("Finding these is the hard part of cryptography (DLP), but we input the known solutions.")
    x = get_integer_input("Enter exponent X (e.g., 1002): ")
    y = get_integer_input("Enter exponent Y (e.g., 3996): ")

    # 3. Get Potential Secret Values (h)
    print("\n[Input 5: POTENTIAL SECRETS (h)]")
    h_input = input("Enter potential secret values (h) to check, separated by commas (e.g., 7538, 7557): ")
    try:
        potential_secrets = [int(val.strip()) for val in h_input.split(',')]
    except ValueError:
        print("❌ Invalid format for potential secrets. Please enter integers separated by commas.")
        return

    # --- Calculation ---
    
    # The order of the group Z_p* is phi(p) = p - 1.
    modulus_exponent = p - 1 

    # 4. Compute the effective exponent (x * y) mod (p - 1)
    xy_product = x * y
    xy_mod_phi = xy_product % modulus_exponent
    
    print(f"\n--- Calculation Steps ---")
    print(f"1. Effective Exponent (Used in Modular Exponentiation):")
    print(f"   (X * Y) mod (P-1) = ({x} * {y}) mod {modulus_exponent} = {xy_mod_phi}")

    # 5. Compute the true shared secret: g^(x*y) mod p
    # This is the value that an honest participant would calculate.
    shared_secret = pow(g, xy_mod_phi, p)
    
    print(f"2. Calculated True Shared Secret (G^XY mod P):")
    print(f"   {g}^{xy_mod_phi} mod {p} = {shared_secret}\n")

    # 6. Check against the given potential secrets (h)
    print(f"--- Decisional Diffie-Hellman Verification ---")
    print("The DDH problem is deciding which 'h' equals the true shared secret.")
    for h in potential_secrets:
        is_match = shared_secret == h
        status = "✅ YES" if is_match else "❌ NO"
        
        print(f"Is G^XY ≡ {h} (mod {p})? {status}")

# Execute the interactive check
if __name__ == "__main__":
    check_ddh_problem_interactive()
    