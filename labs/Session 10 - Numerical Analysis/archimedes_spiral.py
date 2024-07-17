# archimedes_spiral.py
# This  program calculates the arc length of an Archimedes spiral, r=θ from 0 ≤ θ ≤ 8π
# and visualizes the spiral. It defines archimedes_spiral(theta) to compute the radius, 
# and integrand(theta) to compute the integrand sqrt(1+θ^2) for the arc length calculation. 
# The compute_arc_length(a, b) function uses SciPy's quad for numerical integration to find the arc length. 
# The plot_spiral(a, b, arc_length, num_points) function plots the spiral and displays the calculated arc length using Matplotlib.

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def archimedes_spiral(theta):
    """
    Computes the Archimedes spiral function r = theta.

    Parameters:
    theta (float): The input angle(s).

    Returns:
    float or ndarray: The radius corresponding to the input angle(s).
    """
    return theta

def integrand(theta):
    """
    Computes the integrand sqrt((dr/dtheta)^2 + r^2) for the arc length calculation.

    Parameters:
    theta (float): The input angle.

    Returns:
    float: The value of the integrand at the input angle.
    """
    r = archimedes_spiral(theta)
    dr_dtheta = 1  # Since dr_dtheta = 1 for r = theta
    return np.sqrt(dr_dtheta**2 + r**2)

def compute_arc_length(a, b):
    """
    Computes the arc length of the Archimedes spiral from angle a to b.

    Parameters:
    a (float): The lower limit of the angle.
    b (float): The upper limit of the angle.

    Returns:
    float: The arc length of the Archimedes spiral over [a, b].
    """
    arc_length, _ = quad(integrand, a, b)
    return arc_length

def plot_spiral(a, b, arc_length, num_points=1000):
    """
    Plots the Archimedes spiral from angle a to b and displays the arc length on the plot.

    Parameters:
    a (float): The lower limit of the angle.
    b (float): The upper limit of the angle.
    arc_length (float): The computed arc length of the spiral.
    num_points (int): The number of points to use for plotting the spiral.
    """
    theta = np.linspace(a, b, num_points)
    r = archimedes_spiral(theta)
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    plt.figure(figsize=(8, 8))
    plt.plot(x, y, label=r"$r=\theta$")
    plt.title("Archimedes Spiral")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.axis('equal')

    # Adding arc length to the plot
    plt.text(0.95, 0.95, f"Arc length: {arc_length:.14f}", fontsize=12,
             bbox=dict(facecolor='white', alpha=0.5), horizontalalignment='right',
             verticalalignment='top', transform=plt.gca().transAxes)

    plt.show()

def main():
    """
    Main function to compute the arc length of an Archimedes spiral and plot the spiral.
    """
    a, b = 0, 8 * np.pi

    arc_length = compute_arc_length(a, b)

    plot_spiral(a, b, arc_length)

if __name__ == "__main__":
    main()
