# diffie_hellman_interactive.py

def get_integer_input(prompt):
    """Helper function to safely get integer input."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Invalid input. Please enter a valid integer.")

def diffie_hellman_exchange_interactive():
    """
    Simulates the Diffie-Hellman Key Exchange with user-defined inputs, 
    including guidance on input requirements.
    """
    print("\n--- Diffie-Hellman Key Exchange Setup ---")
    
    # 1. Get Public Parameters (P and G)
    print("\n[Input 1: PRIME MODULUS (P)]")
    print("P must be a large prime number (e.g., 2048 bits or more for real security).")
    print("For this demonstration, use a small prime like 23.")
    p = get_integer_input("Enter the large prime modulus (P): ")
    
    print("\n[Input 2: GENERATOR (G)]")
    print("G must be a primitive root modulo P. This ensures the keys cycle through all possible values.")
    print("For P=23, G=5 is a common choice. For this demonstration, use a small integer like 5 or 2.")
    g = get_integer_input("Enter the generator/primitive root (G): ")

    # 2. Get Private Keys (a and b)
    print("\n[Input 3 & 4: PRIVATE KEYS (a and b)]")
    print("a and b must be large, random integers (usually less than P-1).")
    print("For this demonstration, use small integers like 6 and 15.")
    a = get_integer_input("Enter Alice's private key (a): ")
    b = get_integer_input("Enter Bob's private key (b): ")
    
    print(f"\nPublic Parameters: P = {p}, G = {g}")
    print(f"Private Keys: Alice's a = {a}, Bob's b = {b}\n")

    # --- Exchange Begins ---

    # 3. Compute Public Keys (A and B)
    A = pow(g, a, p)
    B = pow(g, b, p)
    
    print(f"--- 1. Public Key Exchange (A = G^a mod P, B = G^b mod P) ---")
    print(f"Alice sends A: {A}")
    print(f"Bob sends B: {B}\n")

    # 4. Compute Shared Secrets (K_A and K_B)
    K_A = pow(B, a, p) # Alice computes (G^b)^a mod p
    K_B = pow(A, b, p) # Bob computes (G^a)^b mod p
    
    print(f"--- 2. Shared Secret Calculation ---")
    print(f"Alice's secret K_A = {K_A}")
    print(f"Bob's secret K_B = {K_B}\n")

    # Final Check
    if K_A == K_B:
        print(f"RESULT: Shared secrets match! The secret key is K = {K_A} 🔐")
    else:
        print("RESULT: Shared secrets do NOT match. Check inputs. ❌")

# Execute the interactive exchange
if __name__ == "__main__":
    diffie_hellman_exchange_interactive()