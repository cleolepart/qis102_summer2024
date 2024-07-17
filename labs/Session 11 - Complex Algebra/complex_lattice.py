# complex_lattice.py

# This code was generated, improved and/or corrected with the assistance of ChatGPT4o.

# This Python script defines a class ComplexLattice that calculates and visualizes a complex function 
# f(z)=z^2 + iz + 1 over a specified range of real (-4 ≤ Re(z) ≤ 4) and imaginary parts (0 ≤ Im(z) ≤ 2). 
# The count of Gaussian integers, z, that satisfy given conditions (|Re(f(z))|, |Im(f(z))| ≤ 10) on f(z) are calculated and displayed.

import numpy as np
import matplotlib.pyplot as plt

class ComplexLattice:
    """
    A class to represent the complex function lattice and plot its results.

    Attributes:
    -----------
    x_values : np.ndarray
        Array of x values.
    y_values : np.ndarray
        Array of y values.
    real_results : list
        List of real parts of f(z).
    imag_results : list
        List of imaginary parts of f(z).
    count : int
        Count of Gaussian integers where |Re(f(z))| <= 10 and |Im(f(z))| <= 10.

    Methods:
    --------
    f_z(x, y):
        Calculates the real and imaginary parts of f(z).
    calculate_results():
        Calculates the results for the given range of x and y values.
    plot_results():
        Plots the scatter plot of the results.
    count_gaussian_integers():
        Counts the Gaussian integers satisfying the given conditions.
    display_count():
        Displays the count of Gaussian integers on the plot.
    """

    def __init__(self):
        """Initializes the ComplexLattice with given ranges for x and y."""
        self.x_values = np.arange(-4, 5, 0.1)
        self.y_values = np.arange(0, 3, 0.1)
        self.real_results = []
        self.imag_results = []
        self.count = 0

    @staticmethod
    def f_z(x, y):
        """
        Calculates the real and imaginary parts of f(z).

        Parameters:
        -----------
        x : float
            Real part of z.
        y : float
            Imaginary part of z.

        Returns:
        --------
        real_part : float
            Real part of f(z).
        imag_part : float
            Imaginary part of f(z).
        """
        real_part = x**2 - y**2 - y + 1
        imag_part = 2 * x * y + x
        return real_part, imag_part

    def calculate_results(self):
        """Calculates the results for the given range of x and y values."""
        for x in self.x_values:
            for y in self.y_values:
                real, imag = self.f_z(x, y)
                self.real_results.append(real)
                self.imag_results.append(imag)

    def count_gaussian_integers(self):
        """Counts the Gaussian integers satisfying the given conditions."""
        x_values = np.arange(-4, 5, 1)
        y_values = np.arange(1, 3, 1)  # y > 0
        for x in x_values:
            for y in y_values:
                real, imag = self.f_z(x, y)
                if abs(real) <= 10 and abs(imag) <= 10:
                    self.count += 1

    def plot_results(self):
        """Plots the scatter plot of the results."""
        plt.figure(figsize=(8, 8))
        plt.scatter(self.real_results, self.imag_results,
                    c=np.abs(self.real_results) + np.abs(self.imag_results),
                    cmap='viridis', alpha=0.5)
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.title(r'$f(z) = z^2 + iz + 1$')
        plt.xlabel('Re $z$')
        plt.ylabel('Im $z$')
        self.display_count()
        plt.show()

    def display_count(self):
        """Displays the count of Gaussian integers on the plot."""
        plt.figtext(0.5, 0.01,
                    f"Number of Gaussian integers z where |Re(f(z))| <= 10 and |Im(f(z))| <= 10: {self.count}",
                    fontsize=12, bbox=dict(facecolor='white', alpha=0.5), horizontalalignment='center')

def main():
    """Main function to run the complex lattice calculations and plotting."""
    lattice = ComplexLattice()
    lattice.calculate_results()
    lattice.count_gaussian_integers()
    lattice.plot_results()

if __name__ == "__main__":
    main()
