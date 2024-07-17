# werner_formula.py

# This script plots four functions on a single graph:
# 1. f1(x) = sin(0.8 * x)
# 2. f2(x) = sin(0.5 * x)
# 3. f3(x) = f1(x) * f2(x)
# 4. f4(x) = Werner's Product-to-sum formula for f1(x) * f2(x)

# The domain for the functions is -3π ≤ x ≤ 3π, subdivided into 100 equally spaced intervals.
# The fourth function is plotted using grey open circle markers, without a connecting line.
# As per instructions, LaTeX is used to populate the legend labels for each curve.

# The assistance of ChatGPT4o was used to generate this documentation.

import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    """
    Calculate the value of f1(x) = sin(0.8 * x).

    Parameters:
    x (array-like): Input values.

    Returns:
    array-like: Output values of f1(x).
    """
    return np.sin(0.8 * x)

def f2(x):
    """
    Calculate the value of f2(x) = sin(0.5 * x).

    Parameters:
    x (array-like): Input values.

    Returns:
    array-like: Output values of f2(x).
    """
    return np.sin(0.5 * x)

def f3(x):
    """
    Calculate the value of f3(x) = f1(x) * f2(x).

    Parameters:
    x (array-like): Input values.

    Returns:
    array-like: Output values of f3(x).
    """
    return f1(x) * f2(x)

def f4(x):
    """
    Calculate the value of Werner's Product-to-sum formula for f1(x) * f2(x).

    f4(x) = 0.5 * (cos((0.8 - 0.5) * x) - cos((0.8 + 0.5) * x))

    Parameters:
    x (array-like): Input values.

    Returns:
    array-like: Output values of f4(x).
    """
    return 0.5 * (np.cos((0.8 - 0.5) * x) - np.cos((0.8 + 0.5) * x))

# Define the domain
x = np.linspace(-3 * np.pi, 3 * np.pi, 100)

# Calculate the functions
y1 = f1(x)
y2 = f2(x)
y3 = f3(x)
y4 = f4(x)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label=r'$f_1(x)=\sin(0.8x)$')
plt.plot(x, y2, label=r'$f_2(x)=\sin(0.5x)$')
plt.plot(x, y3, label=r'$f_3(x)=f_1(x) \cdot f_2(x)$')
plt.plot(x, y4, 'o', color='grey', label=r'$f_4(x)=0.5(\cos((0.8-0.5)x) - \cos((0.8+0.5)x))$')

# Add legend
plt.legend()

# Add grid and labels
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.title('Plot of $f_1(x)$, $f_2(x)$, $f_3(x)$, and $f_4(x)$')
plt.grid(True)

# Show the plot
plt.show()
