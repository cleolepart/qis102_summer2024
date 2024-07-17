# agnesi_witch.py

# This program defines the function for Maria Agnesi's "witch" using the simplified equation with a = 1/2, i.e. 1/(1 + x^2).
# In order to compare the accuracy of approximating a polynomial by including successively more terms, f(x) is defined a power series over −1<x<1.
# Then the exact value of f(x) is plotted over −1.5 < x < 1.5. Overlaid by the plot of the power series ((-1)^n * x^(2n))
# approximations with 2 to 7 terms on the same graph from -1.0 < x < 1.0. 
# Finally a comment block is included explaining the divergence and Runge's Phenomenon.

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    """
    Define the exact function for the Witch of Agnesi with a = 1/2.
    
    Parameters:
        x (numpy.ndarray): Input array of x values.
    
    Returns:
        numpy.ndarray: Output array of y values.
    """
    return 1 / (1 + x**2)

def f_power_series(x, terms):
    """
    Compute the power series approximation of f(x).
    
    Parameters:
        x (numpy.ndarray): Input array of x values.
        terms (int): Number of terms to include in the power series.
    
    Returns:
        numpy.ndarray: Output array of approximated y values.
    """
    series_sum = 0
    for n in range(terms):
        series_sum += ((-1)**n * x**(2*n))
    return series_sum

# Define the x range for the plot
x_values = np.linspace(-1.5, 1.5, 400)
x_values_series = np.linspace(-1.0, 1.0, 400)
y_exact = f(x_values)

# Plot the exact function
plt.plot(x_values, y_exact, label='Exact')

# Plot the power series approximations
for terms in range(2, 8):
    y_series = f_power_series(x_values, terms)
    plt.plot(x_values_series, y_series, label=f'{terms} terms')

# Add plot details
plt.title("Runge's Phenomenon (Witch of Agnesi)")
plt.xlabel("x")
plt.ylabel("y")
plt.axvline(-1, color='black', linestyle='--')
plt.axvline(1, color='black', linestyle='--')
plt.ylim(-2.0, 2.0)
plt.xlim(-1.5, 1.5)
plt.legend()
plt.grid(True)

# Show the plot
plt.show()

"""
Explanation:
1. Divergence near x = -1 and x = 1:
   The power series approximation for the Witch of Agnesi quickly diverges as we approach x = -1 or x = 1 (https://en.wikipedia.org/wiki/Witch_of_Agnesi). 
   This is because the series expansion is only valid within a certain interval around the center (x = 0). As we move closer to the endpoints of the interval, 
   higher-order terms in the series become significant, causing large deviations from the exact function.

2. Runge's Phenomenon (https://en.wikipedia.org/wiki/Runge%27s_phenomenon):
   Runge's Phenomenon describes the oscillatory behavior observed when using polynomial interpolation with equidistant points. In the case of the Witch of Agnesi, as we add more terms to the power series, the approximation initially improves near the center but starts to oscillate and diverge significantly near the endpoints. This behavior is indicative of Runge's Phenomenon, where adding more terms to the polynomial approximation does not necessarily lead to better accuracy, especially near the boundaries of the interval.
"""
