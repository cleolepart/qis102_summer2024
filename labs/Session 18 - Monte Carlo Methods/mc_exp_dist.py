# mc_exp_dist.py

# This code was generated, improved and/or corrected with the assistance of ChatGPT4o and/or Claude 3.5.

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

class MonteCarloExponential:
    def __init__(self, rate_parameter, time_limit, num_samples):
        """
        Initialize the Monte Carlo simulation parameters.

        Parameters:
        rate_parameter (float): Rate parameter (lambda) for the exponential distribution.
        time_limit (float): The time limit to check the probability against.
        num_samples (int): The number of random samples to generate.
        """
        self.rate_parameter = rate_parameter
        self.time_limit = time_limit
        self.num_samples = num_samples
        self.random_samples = np.array([])
        self.estimated_probability = 0.0
        self.exact_probability = 0.0
        self.percent_relative_error = 0.0

    def generate_samples(self):
        """
        Generate random samples from the exponential distribution.
        """
        self.random_samples = np.random.exponential(scale=1/self.rate_parameter, size=self.num_samples)

    def calculate_exact_probability(self):
        """
        Calculate the exact probability using the CDF of the exponential distribution.
        """
        self.exact_probability = expon.cdf(self.time_limit, scale=1/self.rate_parameter)

    def estimate_probability(self):
        """
        Estimate the probability using Monte Carlo simulation.
        """
        below_curve = self.random_samples[self.random_samples <= self.time_limit]
        self.estimated_probability = len(below_curve) / self.num_samples

    def calculate_percent_relative_error(self):
        """
        Calculate the percent relative error of the Monte Carlo estimate.
        """
        self.percent_relative_error = abs((self.estimated_probability - self.exact_probability) / self.exact_probability) * 100

    def plot_results(self):
        """
        Plot the PDF of the exponential distribution, the histogram of the random samples, and the Monte Carlo estimation results.
        """
        x = np.linspace(0, max(self.random_samples), 1000)
        pdf_values = expon.pdf(x, scale=1/self.rate_parameter)

        below_curve = self.random_samples[self.random_samples <= self.time_limit]
        above_curve = self.random_samples[self.random_samples > self.time_limit]

        plt.figure(figsize=(12, 8))
        plt.plot(x, pdf_values, label='Exponential PDF', color='blue')
        plt.hist(self.random_samples, bins=100, density=True, alpha=0.6, color='gray', label='Random Samples Histogram')
        plt.scatter(below_curve, np.zeros_like(below_curve), color='green', s=1, label='Below Time Limit')
        plt.scatter(above_curve, np.zeros_like(above_curve), color='red', s=1, label='Above Time Limit')
        plt.axvline(self.time_limit, color='purple', linestyle='--', label='Time Limit (1 hour)')
        plt.title('Monte Carlo Estimation of Exponential Distribution Probability')
        plt.xlabel('Time (hours)')
        plt.ylabel('Probability Density')
        plt.legend()

        # Display results on the plot
        plt.annotate(f"Estimated Probability: {self.estimated_probability:.4f}", 
             xy=(0.5, 0.15), xycoords='axes fraction',
             fontsize=12, bbox=dict(facecolor='white', alpha=0.5))
        plt.annotate(f"Exact Probability: {self.exact_probability:.4f}", 
             xy=(0.5, 0.10), xycoords='axes fraction',
             fontsize=12, bbox=dict(facecolor='white', alpha=0.5))
        plt.annotate(f"Percent Relative Error: {self.percent_relative_error:.2f}%", 
             xy=(0.5, 0.05), xycoords='axes fraction',
             fontsize=12, bbox=dict(facecolor='white', alpha=0.5))
        plt.show()

    def run_simulation(self):
        """
        Run the full Monte Carlo simulation and plot the results.
        """
        self.generate_samples()
        self.calculate_exact_probability()
        self.estimate_probability()
        self.calculate_percent_relative_error()
        self.plot_results()

if __name__ == "__main__":
    # Parameters
    rate_parameter = 1 / 90  # rate parameter (lambda) for the exponential distribution in hours
    time_limit = 1  # time limit in hours
    num_samples = 25000

    # Create an instance of the MonteCarloExponential class and run the simulation
    mc_simulation = MonteCarloExponential(rate_parameter, time_limit, num_samples)
    mc_simulation.run_simulation()
