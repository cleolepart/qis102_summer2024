# lead_attenuation.py

# This code was generated, improved and/or corrected with the assistance of ChatGPT4o.

# This program reads photon energy and attenuation factor data from a CSV file, 
# creating arrays for photon energies and corresponding attenuation factors. 
# Using cubic interpolation, the script generates a smooth function to estimate attenuation factors for a fine grid of 1000 evenly spaced energy values. 
# It calculates the attenuation coefficient for a photon with 4.65 MeV energy by evaluating the interpolated function at this energy. 
# To determine the percent of photons passing through a 2 cm thick lead shield, it applies the Beer-Lambert law, I/I_0 = e^(−μx),
# where μ is the attenuation coefficient and x is the material thickness, and converts the result to a percentage. 
# The original data points and the interpolated curve are plotted on a logarithmic y-axis scale, with statements of attention coefficient found and percent photons transmitted.

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from pathlib import Path

def main():
    """
    Main function to read photon energy and attenuation factor data from a file,
    interpolate the data, plot the data and the interpolation, and calculate the
    attenuation coefficient for a specific photon energy.
    """
    file_name = "lead_attenuation.csv"
    file_path = Path(__file__).parent / file_name
    
    # Read the lead attenuation data from the CSV file
    data = np.genfromtxt(file_path, delimiter=",")
    energy, attenuation_factor = data.T
    
    # Interpolate the attenuation factor data using cubic interpolation
    attenuation_f = interp1d(energy, attenuation_factor, kind="cubic")
    energy_est = np.linspace(energy.min(), energy.max(), 1000)
    attenuation_est = attenuation_f(energy_est)
    
    # Calculate the attenuation coefficient for a photon with 4.65 MeV energy
    energy_specific = 4.65
    attenuation_specific = attenuation_f(energy_specific)
    print(f"Attenuation coefficient at {energy_specific} MeV: {attenuation_specific:.6f}")
    
    # Calculate the percent of photons passing through a 2 cm thick lead shield
    thickness = 2  # cm
    percent_transmitted = np.exp(-attenuation_specific * thickness) * 100
    print(f"Percent of photons passing through a {thickness} cm thick lead shield: {percent_transmitted:.2f}%")
    
    # Plot the attenuation factor as a function of photon energy
    plt.figure(Path(__file__).name)
    plt.scatter(energy, attenuation_factor, label="Data points")
    plt.plot(energy_est, attenuation_est, color="black", label="Interpolated curve")
    plt.yscale("log")
    plt.xlabel("Photon Energy (MeV)")
    plt.ylabel("Attenuation Factor, $\mu  (cm^{-1})$")
    plt.title("Lead Shield Attenuation Factor vs Photon Energy")
    
    # Ensure top y-axis data point appears with scale mark
    y_ticks = [10**i for i in range(int(np.floor(np.log10(min(attenuation_factor)))), int(np.ceil(np.log10(max(attenuation_factor))) + 1))]
    plt.yticks(y_ticks)

    # Add the calculated information to the plot
    textstr = '\n'.join((
        f'Attenuation coefficient at {energy_specific} MeV: {attenuation_specific:.6f}',
        f'Percent transmitted through {thickness} cm: {percent_transmitted:.2f}%'
    ))
    plt.gcf().text(0.25, 0.55, textstr, fontsize=12, bbox=dict(facecolor='white', alpha=0.5))

    plt.legend()
    plt.show()

# Execute the main function
if __name__ == "__main__":
    main()
