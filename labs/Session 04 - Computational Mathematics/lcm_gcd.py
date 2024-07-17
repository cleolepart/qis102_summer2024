#lcm_gcd.py
import math

def lcm(a, b):
    """
    Calculate the Lowest Common Multiple (LCM) of two integers.

    The LCM of two integers a and b is given by the formula:
    LCM(a, b) = |a * b| / GCD(a, b)

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The LCM of the two integers.
    """
    return abs(a * b) // math.gcd(a, b)

def main():
    """
    Main function to calculate and display the LCM of two specific integers.

    The user-defined integers in this example are 447618 and 2011835.
    """
    # Define the two integers
    num1 = 447618
    num2 = 2011835
    
    # Calculate the LCM of num1 and num2
    result = lcm(num1, num2)
    
    # Display the result
    print(f"The LCM of {num1} and {num2} is {result}")

if __name__ == "__main__":
    main()
