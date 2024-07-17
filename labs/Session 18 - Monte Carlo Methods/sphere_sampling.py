# sphere_sampling.py
# This code was generated, improved and/or corrected with the assistance of Claude 3.5.

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

def plot_sphere(ax, u, v, title, equation):
    """
    Plots a 3D scatter plot of points on a sphere.

    Parameters:
    ax (Axes3D): The 3D axis to plot on.
    u (ndarray): Array of angle u values.
    v (ndarray): Array of angle v values.
    title (str): Title of the plot.
    equation (str): Equation used for generating the points, to be displayed on the plot.
    """
    x = np.sin(u) * np.cos(v)
    y = np.sin(u) * np.sin(v)
    z = np.cos(u)
    ax.scatter(x, y, z, s=0.5)
    ax.set_title(title)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_aspect("equal")
    # Add equation text to the plot
    ax.text2D(0.05, 0.95, equation, transform=ax.transAxes, fontsize=9, verticalalignment='top', bbox=dict(facecolor='white', alpha=0.8))

def main():
    """
    Main function to create and display plots of points sampled on a sphere.
    Demonstrates both non-uniform and uniform sampling techniques.
    """
    # Create random samples
    n = 15000

    # Non-uniform sampling
    u_non_uniform = np.random.rand(n) * np.pi
    v_non_uniform = np.random.rand(n) * 2 * np.pi

    # Uniform sampling
    u_uniform = np.arccos(2 * np.random.rand(n) - 1)
    v_uniform = np.random.rand(n) * 2 * np.pi

    # Create the plot
    fig = plt.figure(figsize=(16, 8))

    # Non-uniform plot
    ax1 = fig.add_subplot(121, projection='3d')
    plot_sphere(ax1, u_non_uniform, v_non_uniform, "Non-uniform Sampling", "u = rand() * π")
    ax1.view_init(azim=-72, elev=48)

    # Uniform plot
    ax2 = fig.add_subplot(122, projection='3d')
    plot_sphere(ax2, u_uniform, v_uniform, "Uniform Sampling", "u = arccos(2 * rand() - 1)")
    ax2.view_init(azim=-72, elev=48)

    # Add explanation text
    explanation = "Uniform sampling compensates for smaller surface area near poles."
    plt.figtext(0.5, 0.02, explanation, ha='center', va='center', bbox=dict(facecolor='white', alpha=0.8), fontsize=10)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
