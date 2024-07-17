# harmonograph.py

# This script simulates a two-pendulum harmonograph and visualizes the resulting pattern.

# The script uses scipy's solve_ivp to solve the differential equations that describe
# the pendulum motion, and matplotlib to plot the results.

# To modify the harmonograph pattern:
# - Adjust the pendulum lengths, initial angles, and angular velocities in the main() function.
# - Change the time range of the simulation by modifying time_initial and time_final.

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator
from scipy.integrate import solve_ivp


def model(time, state_vector, phase_constant):
    """
    Defines the differential equations for the pendulum motion.

    Args:
    time (float): The current time (not used in this model, but required by solve_ivp).
    state_vector (list): A list containing [omega, theta], where omega is angular velocity
                         and theta is the angle of the pendulum.
    phase_constant (float): A constant determined by pendulum length and gravity.

    Returns:
    tuple: The derivatives (d_omega, d_theta) representing the change in angular velocity
           and angle respectively.
    """
    omega, theta = state_vector
    d_omega = -phase_constant * np.sin(theta)
    d_theta = omega
    return d_omega, d_theta


def main():
    """
    The main function that sets up the harmonograph simulation and creates the plot.

    This function:
    1. Sets initial conditions for two pendulums (length, initial angle, initial angular velocity).
    2. Calculates the phase constants for each pendulum.
    3. Defines the time range for the simulation.
    4. Uses solve_ivp to calculate the trajectories of both pendulums.
    5. Ensures the resulting data for both pendulums is of equal length.
    6. Plots the harmonograph pattern using matplotlib.
    """
    # Set Initial Conditions
    pendulum1_length = 1.0  # meters
    theta1_initial = np.radians(30)  # degrees
    omega1_initial = 0.00  # radians/sec

    pendulum2_length = 0.95  # meters
    theta2_initial = np.radians(10)  # degrees
    omega2_initial = 0.3  # radians/sec

    # Precalculate phase constants
    phase1_constant = 9.81 / pendulum1_length
    phase2_constant = 9.81 / pendulum2_length

    # Set model duration (seconds)
    time_initial = 1.0
    time_final = 3.0

    # Calculate trajectory of 1st pendulum
    sol = solve_ivp(
        model,
        (time_initial, time_final),
        [omega1_initial, theta1_initial],
        max_step=0.01,
        args=(phase1_constant,),
    )
    theta1 = sol.y[1]

    # Calculate trajectory of 2nd pendulum
    sol = solve_ivp(
        model,
        (time_initial, time_final),
        [omega2_initial, theta2_initial],
        max_step=0.01,
        args=(phase2_constant,),
    )
    theta2 = sol.y[1]

    # Ensure both vectors are same length
    if len(theta1) > len(theta2):
        theta1 = theta1[: len(theta2)]
    else:
        theta2 = theta2[: len(theta1)]

    plt.figure(Path(__file__).name)
    plt.plot(theta1, theta2, color="blue", lw=2)
    plt.title("Two Pendulum Harmonograph")
    plt.gca().xaxis.set_minor_locator(AutoMinorLocator())
    plt.gca().yaxis.set_minor_locator(AutoMinorLocator())
    plt.tight_layout()
    plt.show()

main()
