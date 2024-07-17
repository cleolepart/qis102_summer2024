# rlc_circuit.py

# This script defines the RLC circuit's second-order ODE as a system of first-order ODEs;
# uses the solve_ivp function from SciPy to numerically solve the system over the time span of 0 to 1 second;
# plots the current over time.

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def rlc_ode(t, y, R, L, C):
    I, dI_dt = y
    d2I_dt2 = -R/L * dI_dt - 1/(L*C) * I
    return [dI_dt, d2I_dt2]

def main():
    # Define constants
    R = 0.1  # Ohms
    L = 0.01  # Henries
    C = 0.01  # Farads

    # Initial conditions
    I_initial = 1.0  # Amps
    dI_dt_initial = 0.0  # Initial rate of change of current

    # Time span for the simulation
    t_span = (0, 1)  # From 0 to 1 second
    t_eval = np.linspace(t_span[0], t_span[1], 1000)  # Time points to evaluate

    # Solve the ODE
    sol = solve_ivp(
        rlc_ode,
        t_span,
        [I_initial, dI_dt_initial],
        args=(R, L, C),
        t_eval=t_eval
    )

    # Extract the solution
    I_t = sol.y[0]
    t = sol.t

    # Plot the result
    plt.figure()
    plt.plot(t, I_t, label='Current (I)')
    plt.title('Current Over Time in an RLC Circuit')
    plt.xlabel('Time (s)')
    plt.ylabel('Current (A)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
