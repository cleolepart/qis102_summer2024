# kinematics_regression.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    """
    Main function to execute the kinematics regression analysis.
    """
    # Load the data from the CSV file
    data = pd.read_csv('/Users/clepart/qis102/labs/Session 16 - Simulation and Modeling/kinematics_regression.csv')
    times = data['time'].values
    distances = data['distance'].values

    # Prepare the design matrix for the quadratic regression
    X = np.vstack([times, 0.5 * times**2]).T
    y = distances

    # Perform the least squares regression to find v0 and a
    coefficients, _, _, _ = np.linalg.lstsq(X, y, rcond=None)
    v0, a = coefficients

    # Display the results
    print(f"Initial velocity (v0): {v0:.2f} m/s")
    print(f"Constant acceleration (a): {a:.2f} m/s^2")

    # Plot the original data
    plt.scatter(times, distances, label='Data', color='blue')

    # Generate smooth curve data for the fit
    time_fit = np.linspace(min(times), max(times), 100)
    distance_fit = v0 * time_fit + 0.5 * a * time_fit**2

    # Plot the fitted curve
    plt.plot(time_fit, distance_fit, label='Fit', color='red')

    # Annotate the graph with initial velocity and acceleration
    plt.annotate(f'Initial velocity ($v_0$): {v0:.2f} m/s\nAcceleration ($a$): {a:.2f} m/s$^2$',
             xy=(0.05, 0.95), xycoords='axes fraction',
             fontsize=10, backgroundcolor='white', verticalalignment='top')

    # Add labels and title
    plt.xlabel('Time (s)')
    plt.ylabel('Distance (m)')
    plt.title('Kinematics Regression')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
