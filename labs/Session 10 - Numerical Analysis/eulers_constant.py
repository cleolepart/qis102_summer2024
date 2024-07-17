# eulers_constant.py

# This code was generated, improved and/or corrected with the assistance of ChatGPT4o.

# This program estimates Euler's constant (γ) using SciPy's quad function to numerically 
# integrate the given integral. The estimated value of γ is then used to generate a plot. 
# The function harmonic_numbers(n) generates the first n Harmonic numbers using NumPy's cumsum function. 
# The plot_graph(gamma) function creates the plot with γ + ln(x) as a line graph and the first 50 Harmonic numbers as a step plot. 
# The plt.step function is used for the step plot, with the where='mid' argument to ensure the steps align correctly with the x-values. 
# The main() function estimates Euler's constant and then calls plot_graph(gamma) to display the plot.

import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

def estimate_eulers_constant():
    """
    Numerically estimate Euler's constant (γ) using the integral:
    γ = - ∫_0^1 ln(ln(1/x)) dx

    Returns:
        float: The estimated value of Euler's constant (γ).
    """
    integrand = lambda x: np.log(np.log(1/x))
    gamma, _ = integrate.quad(integrand, 0, 1)
    return -gamma

def harmonic_numbers(n):
    """
    Generate the first n Harmonic numbers.

    Args:
        n (int): The number of Harmonic numbers to generate.

    Returns:
        numpy.ndarray: An array of the first n Harmonic numbers.
    """
    H = np.cumsum(1.0 / np.arange(1, n + 1))
    return H

def plot_graph(gamma):
    """
    Plot γ + ln(x) and the first 50 Harmonic numbers.

    Args:
        gamma (float): The estimated value of Euler's constant (γ).

    Returns:
        None
    """
    x = np.linspace(1, 50, 500)
    y_gamma_ln_x = gamma + np.log(x)
    
    H = harmonic_numbers(50)
    
    plt.figure(figsize=(10, 6))
    
    plt.plot(x, y_gamma_ln_x, label='$\gamma + \ln(x)$', color='blue')
    plt.step(np.arange(1, 51), H, where='mid', label='Harmonic Numbers', color='orange')
    
    plt.xlabel('x')
    plt.ylabel('Value')
    plt.title('Graph of $\gamma + \ln(x)$ and the first 50 Harmonic Numbers')
    plt.legend()
    plt.grid(True)
    
    # Add the estimated value of Euler's constant to the graph
    plt.text(30, 2, f"Estimated $\gamma$: {gamma:.6f}", fontsize=12, color='black', 
             verticalalignment='bottom', horizontalalignment='right')
    
    plt.show()

def main():
    """
    Main function to estimate Euler's constant and plot the graph.

    Returns:
        None
    """
    gamma = estimate_eulers_constant()
    #print(f"Estimated Euler's constant (γ): {gamma}")
    plot_graph(gamma)

if __name__ == "__main__":
    main()
