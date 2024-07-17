import math

MAX_TERMS = 20

def normalize_cf(cf):
    """
    Normalize the continued fraction terms.
    
    Args:
        cf (list of int): The continued fraction terms.
    
    Returns:
        list of int: The normalized continued fraction terms.
    
    Note: This function is copied from std_cf.py.
    """
    while len(cf) > 2 and cf[-1] == 1 and cf[-2] != 1:
        cf[int(-2)] += 1
        cf.pop(-1)
    return cf

def encode_cf(x, max_terms=7):
    """
    Compute the continued fraction representation of a real number.
    
    Args:
        x (float): The real number to be represented as a continued fraction.
        max_terms (int): The maximum number of terms to display.
    
    Returns:
        list of int: The continued fraction terms.
    
    Note: This function is adapted from std_cf.py.
    """
    cf = []
    while len(cf) < max_terms:
        cf.append(int(x))
        x = x - int(x)
        if x < 1e-11:
            break
        x = 1 / x
    return normalize_cf(cf)

def calculate_x(n):
    """
    Calculate the value of x for a given n using the formula:
    x = (1 + sqrt(4n^2 - 4n + 5)) / 2
    
    Args:
        n (int): The positive integer n.
    
    Returns:
        float: The calculated value of x.
    """
    return (1 + math.sqrt(4 * n ** 2 - 4 * n + 5)) / 2

def main():
    """
    Main function to calculate and display the continued fraction for
    x = (1 + sqrt(4n^2 - 4n + 5)) / 2 for n in {1, 2, ..., 9}.
    """
    print("Continued fractions for x = (1 + sqrt(4n^2 - 4n + 5)) / 2")
    for n in range(1, 10):
        x = calculate_x(n)
        cf = encode_cf(x, max_terms=7)
        print(f"n = {n}: x = {x} -> Continued Fraction: {cf}")

if __name__ == "__main__":
    main()
