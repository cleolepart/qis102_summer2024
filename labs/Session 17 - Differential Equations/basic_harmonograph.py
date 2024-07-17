from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator
from scipy.integrate import solve_ivp

def model(time, state_vector, phase_constant):
    omega, theta = state_vector
    d_omega = -phase_constant * np.sin(theta)
    d_theta = omega
    return d_omega, d_theta

def main():
    # Set Initial Conditions
    pendulum1_length = 1.0  # meters
    theta1_initial = np.radians(30)  # degrees
    omega1_initial = 0.0  # radians/sec

    pendulum2_length = 0.95  # meters
    theta2_initial = np.radians(5)  # degrees
    omega2_initial = 0.3  # radians/sec

    # Precalculate phase constants
    phase1_constant = 9.81 / pendulum1_length
    phase2_constant = 9.81 / pendulum2_length

    # Set model duration (seconds)
    time_initial = 1
    time_final = 3.0  # Adjust this value to get closer to one orbit

    # Calculate trajectory of 1st pendulum
    sol = solve_ivp(
        model,
        (time_initial, time_final),
        [omega1_initial, theta1_initial],
        max_step=0.01,
        args=(phase1_constant,),
    )
    theta1 = sol.y[1]
    time = sol.t

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
        time = time[: len(theta2)]
    else:
        theta2 = theta2[: len(theta1)]

    # Plot the entire calculated trajectory
    plt.figure(Path(__file__).name)
    plt.plot(theta1, theta2, color="blue", lw=2)
    plt.title("Two Pendulum Harmonograph")
    plt.gca().xaxis.set_minor_locator(AutoMinorLocator())
    plt.gca().yaxis.set_minor_locator(AutoMinorLocator())
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout()
    plt.show()
    print(f"Simulation time: {time[-1]:.2f} seconds")

main()