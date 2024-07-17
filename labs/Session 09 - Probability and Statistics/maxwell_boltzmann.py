# maxwell_boltzmann.py
# This code calculates and plots the probability density function (PDF) 
# of the Maxwell-Boltzmann distribution for different parameters 'a'.

import numpy as np
import matplotlib.pyplot as plt

def maxwell_boltzmann_pdf(x, a):
    """
    Calculate the Maxwell-Boltzmann probability density function (PDF).

    Parameters:
    x (numpy.ndarray): Array of values at which to calculate the PDF.
    a (float): Scale parameter of the distribution.

    Returns:
    numpy.ndarray: PDF values for the given x and a.
    """
    return np.sqrt(2/np.pi) * (x**2 * np.exp(-x**2 / (2 * a**2))) / a**3

def plot_maxwell_boltzmann():
    """
    Plot the Maxwell-Boltzmann PDFs for different scale parameters on the same graph.
    """
    x = np.linspace(0, 20, 500)
    
    # Parameters for the PDFs
    params = [1, 2, 5]
    
    plt.figure(figsize=(10, 6))
    
    for a in params:
        y = maxwell_boltzmann_pdf(x, a)
        plt.plot(x, y, label=f'a = {a}')
    
    plt.title('Maxwell-Boltzmann Distribution PDF')
    plt.xlabel('x')
    plt.ylabel('Probability Density')
    plt.xlim(0, 20)
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    plot_maxwell_boltzmann()
