# plot3d_cylinder.py

# This program generates and plots a 3D cylinder using matplotlib.

# The `generate_cylinder` function calculates the cylinder's coordinates based on the specified radius,
# height, and number of points. The vertical positions are represented by `u`, while the angular positions
# around the circumference are represented by `v`. The `x` and `y` coordinates form circles at different heights,
# and `z` replicates the vertical positions across the angular positions.

# The `plot_cylinder` function plots the cylinder in 3D space using the generated coordinates. It sets the grid
# limits for `x` and `y` to -40 and 40, with tick marks every 20 units, and labels the axes appropriately.

# The `main` function orchestrates the generation and plotting of the cylinder by calling `generate_cylinder`
# and `plot_cylinder` with the specified parameters.

# This code was generated, improved and/or corrected with the assistance of ChatGPT4o.

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

def generate_cylinder(radius, height, num_points=30):
    """
    Generates the coordinates for a cylinder aligned along the z-axis.

    Parameters:
        radius (float): The radius of the cylinder.
        height (float): The height of the cylinder.
        num_points (int): The number of points to generate along the height and circumference.

    Returns:
        tuple: Arrays of x, y, z coordinates.
    """
    u = np.linspace(0, height, num_points)  # Vertical location
    v = np.linspace(0, 2 * np.pi, num_points)  # Horizontal circular slice

    x = radius * np.outer(np.ones_like(u), np.cos(v))
    y = radius * np.outer(np.ones_like(u), np.sin(v))
    z = np.outer(u, np.ones_like(v))
    
    return x, y, z

def plot_cylinder(x, y, z, color="red"):
    """
    Plots a 3D cylinder using the provided coordinates.

    Parameters:
        x (ndarray): The x coordinates.
        y (ndarray): The y coordinates.
        z (ndarray): The z coordinates.
        color (str): The color of the cylinder.

    Returns:
        None
    """
    plt.figure(Path(__file__).name)
    ax = plt.axes(projection="3d")
    ax.plot_surface(x, y, z, color=color)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_xlim(-40, 40)
    ax.set_ylim(-40, 40)
    ax.set_zlim(np.min(z), np.max(z))
    ax.set_xticks(np.arange(-40, 41, 20))
    ax.set_yticks(np.arange(-40, 41, 20))
    plt.show()

def main():
    """
    Main function to generate and plot a cylinder.
    
    Returns:
        None
    """
    radius, height = 10, 50
    x, y, z = generate_cylinder(radius, height)
    plot_cylinder(x, y, z)

if __name__ == "__main__":
    main()
