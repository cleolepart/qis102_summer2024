# random_walk_gamma.py
# This code was generated, improved and/or corrected with the assistance of ChatGPT4o.

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma

def expected_distance(N, d):
    """
    Calculate the expected final distance of a uniform random walk on a unit lattice.

    This function uses the formula for the expected (mean) value of the final distance
    from the origin for a random walk of N steps in a d-dimensional space.

    Parameters:
    N (int): Number of steps in the random walk.
    d (float): Dimension of the lattice.

    Returns:
    float: Expected final distance from the origin after N steps.
    """
    return np.sqrt(2 * N / d) * (gamma((d + 1) / 2) / gamma(d / 2)) ** 2

def plot_expected_distance(N, d_min, d_max):
    """
    Plot the expected final distance for dimensions ranging from d_min to d_max.

    This function generates a plot of the expected final distance from the origin
    as a function of the dimension d, using the provided formula. The plot covers
    dimensions from d_min to d_max for a random walk with N steps.

    Parameters:
    N (int): Number of steps in the random walk.
    d_min (float): Minimum dimension for the plot.
    d_max (float): Maximum dimension for the plot.

    Returns:
    None: The function generates and displays the plot.
    """
    d_values = np.linspace(d_min, d_max, 1000)
    
    # Print the first 10 and last 10 values to show they are not just integers
    print(f"First 10 d values: {d_values[:10]}")
    print(f"Last 10 d values: {d_values[-10:]}")
    
    expected_distances = [expected_distance(N, d) for d in d_values]

    plt.figure(figsize=(10, 6))
    plt.plot(d_values, expected_distances, label=f'N = {N}')
    plt.xlabel('Dimension (d)')
    plt.ylabel('Expected Final Distance')
    plt.title('Expected Final Distance of a Uniform Random Walk')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    """
    Main block for the random_walk_gamma.py script.

    This block is executed when the script is run directly. It sets the number of steps
    for the random walk and the range of dimensions to be evaluated. It then calls the
    plot_expected_distance function to generate and display the plot.

    Variables:
    N (int): Number of steps in the random walk (set to 20,000).
    d_min (float): Minimum dimension to evaluate (set to 1).
    d_max (float): Maximum dimension to evaluate (set to 25).

    The function plot_expected_distance is called with these parameters to generate the plot.
    """
    N = 20000
    d_min = 1
    d_max = 25
    plot_expected_distance(N, d_min, d_max)
