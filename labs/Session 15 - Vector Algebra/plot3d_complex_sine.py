# plot3d_complex_sine.py

# This program generates and plots the surface in the complex plane given by
# f(z) = |sin(z)| over the region (±2.5 ± i).

# The region is defined as a rectangular grid in the complex plane with real
# part ranging from -2.5 to 2.5 and imaginary part ranging from -1 to 1.

# This code was generated, improved and/or corrected with the assistance of ChatGPT4o.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def complex_sine_surface(xmin, xmax, ymin, ymax, resolution=100):
    """
    Generates the surface data for the complex sine function.

    Parameters:
        xmin (float): Minimum value of the real part.
        xmax (float): Maximum value of the real part.
        ymin (float): Minimum value of the imaginary part.
        ymax (float): Maximum value of the imaginary part.
        resolution (int): Number of points along each axis.

    Returns:
        tuple: Meshgrid arrays for real part (X), imaginary part (Y), and the magnitude |sin(z)|.
    """
    x = np.linspace(xmin, xmax, resolution)
    y = np.linspace(ymin, ymax, resolution)
    X, Y = np.meshgrid(x, y)
    Z = np.abs(np.sin(X + 1j * Y))
    return X, Y, Z

def plot_surface(X, Y, Z):
    """
    Plots the surface defined by the magnitude of the complex sine function.

    Parameters:
        X (ndarray): Meshgrid array for the real part.
        Y (ndarray): Meshgrid array for the imaginary part.
        Z (ndarray): Magnitude of the complex sine function.

    Returns:
        None
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(X, Y, Z, cmap='coolwarm')
    fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
    ax.set_xlabel('Re(z)')
    ax.set_ylabel('Im(z)')
    ax.set_zlabel('|sin(z)|')
    plt.figtext(0.5, 0.01, r'$f(z) = |\sin(z)|$', ha='center', fontsize=12)
    plt.show()

def main():
    """
    Main function to generate and plot the complex sine surface.

    Returns:
        None
    """
    xmin, xmax = -2.5, 2.5
    ymin, ymax = -1, 1
    X, Y, Z = complex_sine_surface(xmin, xmax, ymin, ymax)
    plot_surface(X, Y, Z)

if __name__ == "__main__":
    main()
