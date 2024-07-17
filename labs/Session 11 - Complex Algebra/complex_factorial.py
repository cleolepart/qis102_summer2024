"""
complex_factorial.py

This code was generated, improved and/or corrected with the assistance of ChatGPT4o and/or Claude.

This script calculates the factorial of the imaginary unit i using SciPy's quad in-built function for integration,
Euler's formula in complex analysis, and the identity x^i = e^{i ln x}. 

The `eulers_formula` function computes e^(i*z) using Euler's formula.
The `integrand` function defines the integrand for the Gamma function in the complex plane, taking the variable of integration t and the complex number z as parameters. 
The `gamma_function` function computes the Gamma function for a complex number using numerical integration, employing the `quad` function from the `scipy.integrate` module to calculate the real and imaginary parts of the integral separately. 
The `complex_factorial` function computes the factorial of a complex number using Euler's Gamma Function by calling the `gamma_function` with the argument z + 1.

For future comparison, Stirling's approximation, sqrt(2πz)*(z/e)^z, is also defined as a function.

In the `main` function, the imaginary unit i is defined and the `complex_factorial` function with i as the argument is called to compute i!. 
For comparison, the 'stirling_approximation' function is also called with arg, i, as well as a check with the SciPy in-built Gamma function on i.
The results of the calculations and comparisons (as absolute difference) are then printed to the console, displaying the approximate value of the factorial of i. 
"""
import numpy as np
from scipy.integrate import quad

from scipy.special import gamma
from tabulate import tabulate
import warnings

def eulers_formula(z):
    """
    Compute e^(i*z) using Euler's formula.
    
    Parameters:
    z (complex): A complex number.
    
    Returns:
    complex: The result of e^(i*z).
    """
    return np.exp(1j * np.log(z))

def integrand(t, z):
    """
    Integrand for the Gamma function in the complex plane.
    
    Parameters:
    t (float): Variable of integration.
    z (complex): Complex number for which to evaluate the integrand.
    
    Returns:
    complex: The integrand value at t for the complex number z.
    """
    return np.exp(-t) * t**(z - 1)

def gamma_function(z):
    """
    Compute the Gamma function for a complex number using numerical integration.
    
    Parameters:
    z (complex): A complex number.
    
    Returns:
    complex: The value of the Gamma function at z.
    """
    real_part, real_error = quad(lambda t: integrand(t, z).real, 0, np.inf)
    imag_part, imag_error = quad(lambda t: integrand(t, z).imag, 0, np.inf)
    return real_part + 1j * imag_part

def complex_factorial(z):
    """
    Compute the factorial of a complex number using Euler's Gamma Function.
    
    Parameters:
    z (complex): A complex number.
    
    Returns:
    complex: The factorial of the complex number.
    """
    return gamma_function(z + 1)

def stirling_approximation(z):
    """
    Compute the factorial of a complex number using Stirling's approximation.
    
    Parameters:
    z (complex): A complex number.
    
    Returns:
    complex: The approximate factorial of the complex number.
    """
    return np.sqrt(2 * np.pi * z) * (z / np.e)**z


def main():
    # Suppress the ComplexWarning
    warnings.filterwarnings('ignore', category=np.ComplexWarning)
    
    # Imaginary unit
    i = 1j
    
    # Compute i! using the custom Gamma function
    factorial_i_gamma = complex_factorial(i)
    
    # Compute i! using Stirling's approximation
    factorial_i_stirling = stirling_approximation(i)
    
    # Compute i! using the gamma function from scipy.special
    factorial_i_scipy = gamma(i + 1)
    
    # Create a table to store the results
    table_data = [
        ["Method", "Result"],
        ["Custom Gamma Function", factorial_i_gamma],
        ["Stirling's Approximation", factorial_i_stirling],
        ["scipy.special.gamma", factorial_i_scipy]
    ]
    
    # Compute the absolute differences
    diff_gamma_stirling = abs(factorial_i_gamma - factorial_i_stirling)
    diff_gamma_scipy = abs(factorial_i_gamma - factorial_i_scipy)
    
    # Add the absolute differences to the table
    table_data.extend([
        ["", ""],
        ["Absolute Differences", ""],
        ["Custom Gamma vs Stirling", diff_gamma_stirling],
        ["Custom Gamma vs scipy.special.gamma", diff_gamma_scipy]
    ])
    
    # Print the table
    print(tabulate(table_data, headers="firstrow"))

if __name__ == "__main__":
    main()
