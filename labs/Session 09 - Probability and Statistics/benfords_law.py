# benfords_law.py
# This code demonstrates Benford's Law by calculating the probability 
# of each digit (1 to 9) appearing as the most significant digit (MSD) 
# in 100,000 very large random integers. The program uses matplotlib.pyplot 
# to create a histogram showing the probability distribution.

# Disclaimer: This code draws heavily on the instructor's stated solution.

import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

def calculate_msd_probabilities(sample_size=100_000, low=1, high=1_000_000, power=100):
    """
    Calculate the probabilities of each digit (1-9) appearing as the most significant digit (MSD)
    in a specified number of large random integers.
    
    Parameters:
        sample_size (int): The number of random integers to generate.
        low (int): The lower bound of the random integers range.
        high (int): The upper bound of the random integers range.
        power (int): The power to which each random integer is raised.
    
    Returns:
        np.ndarray: An array containing the probabilities of digits 1 through 9 appearing as the MSD.
    """
    msd_counts = np.zeros(10)
    for _ in range(sample_size):
        number = random.randint(low, high) ** power
        most_significant_digit = int(str(number)[0])
        msd_counts[most_significant_digit] += 1
    
    msd_probabilities = msd_counts[1:] / sample_size
    return msd_probabilities

def plot_benfords_law(msd_probabilities):
    """
    Plot the probabilities of each digit (1-9) appearing as the MSD against the theoretical Benford's Law distribution.
    
    Parameters:
        msd_probabilities (np.ndarray): An array containing the probabilities of digits 1 through 9 appearing as the MSD.
    """
    digits = range(1, 10)
    theoretical_probabilities = np.log10(1 + 1 / np.array(digits))
    
    plt.figure("Benford's Law")
    plt.bar(digits, msd_probabilities, zorder=2.5, label="Random Data")
    plt.plot(digits, theoretical_probabilities, color="green", lw=3, zorder=3.0, label=r"$\log_{10}\left(1+\frac{1}{d}\right)$")
    plt.title("Benford's Law - Probability Distribution of Most Significant Digit")
    plt.xlabel("Most Significant Digit (MSD)")
    plt.ylabel("Probability of MSD")
    
    ax = plt.gca()
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.legend(loc="upper right")
    ax.grid(True)
    plt.show()

def main():
    """
    Main function to calculate MSD probabilities and plot Benford's Law distribution.
    """
    sample_size = 100_000
    low = 1
    high = 1_000_000
    power = 100
    
    msd_probabilities = calculate_msd_probabilities(sample_size, low, high, power)
    plot_benfords_law(msd_probabilities)

if __name__ == "__main__":
    main()
