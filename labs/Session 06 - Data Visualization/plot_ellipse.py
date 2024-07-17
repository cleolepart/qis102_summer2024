
# plot_ellipse.py
"""
This program plots a 2D graph of an ellipse with the following parameters:
- Major axis of length 100 (along the x-axis)
- Minor axis of length 50 (along the y-axis)
- Centered at the origin

The program calculates the points on the perimeter of the ellipse using polar coordinates,
sweeping theta through the interval [0, 2π). It then converts these polar coordinates
to Cartesian coordinates and graphs them using a line plot.
"""

import numpy as np
import matplotlib.pyplot as plt

def plot_ellipse():
    """
    Plots a 2D graph of an ellipse.

    The ellipse has the following parameters:
    - Major axis length: 100 units
    - Minor axis length: 50 units
    - Centered at the origin (0, 0)

    The function calculates the points on the perimeter of the ellipse using polar coordinates
    and then converts these points to Cartesian coordinates for plotting.
    """
    # Major and minor axes
    a = 100  # Major axis length
    b = 50   # Minor axis length

    # Sweep theta through the interval [0, 2*pi)
    theta = np.linspace(0, 2 * np.pi, 1000)

    # Radius at each theta using the ellipse formula in polar coordinates
    r = (a * b) / np.sqrt((b * np.cos(theta))**2 + (a * np.sin(theta))**2)

    # Convert polar coordinates to Cartesian coordinates
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    # Plot the ellipse
    plt.figure(figsize=(8, 8))
    plt.plot(x, y, label='Ellipse')
    plt.title(r'Ellipse: $\frac{x^2}{100^2} + \frac{y^2}{50^2} = 1$')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.axis('equal') # Ensures the aspect ratio is equal
    plt.show()

if __name__ == "__main__":
    plot_ellipse()
