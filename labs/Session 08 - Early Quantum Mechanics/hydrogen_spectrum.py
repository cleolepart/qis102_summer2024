# hydrogen_spectrum.py
# calculates and displays the wavelengths (in nanometers) 
# for the Pfund and Humphreys spectral series of Hydrogen 
# using both the Rydberg and Bohr formulas.

def rydberg_formula(n1, n2):
    """
    Calculate the wavelength using the Rydberg formula.
    
    Parameters:
    n1 (int): Lower energy level.
    n2 (int): Higher energy level.
    
    Returns:
    float: Wavelength in nanometers.
    """
    R = 1.097373e7  # Rydberg constant in m^-1
    wavelength = 1 / (R * ((1 / n1**2) - (1 / n2**2))) * 1e9  # Convert to nanometers
    return wavelength

def bohr_formula(n1, n2):
    """
    Calculate the wavelength using the Bohr formula.
    
    Parameters:
    n1 (int): Lower energy level.
    n2 (int): Higher energy level.
    
    Returns:
    float: Wavelength in nanometers.
    """
    h = 6.62607015e-34  # Planck's constant in J·s
    c = 3.0e8  # Speed of light in m/s
    e = 1.602176634e-19  # Elementary charge in C
    epsilon0 = 8.854187817e-12  # Vacuum permittivity in F/m
    me = 9.10938356e-31  # Electron mass in kg
    
    rydberg_energy = me * e**4 / (8 * epsilon0**2 * h**2)  # Rydberg energy in J
    energy_difference = rydberg_energy * ((1 / n1**2) - (1 / n2**2))
    wavelength = h * c / energy_difference * 1e9  # Convert to nanometers
    return wavelength

def print_wavelengths(series_name, n1, n2_range):
    """
    Print the wavelengths for a given spectral series.
    
    Parameters:
    series_name (str): Name of the spectral series.
    n1 (int): Lower energy level for the series.
    n2_range (list): Range of higher energy levels.
    """
    print(f"{series_name} Series (n1 = {n1}):")
    print("n2\tRydberg (nm)\tBohr (nm)")
    for n2 in n2_range:
        wavelength_rydberg = rydberg_formula(n1, n2)
        wavelength_bohr = bohr_formula(n1, n2)
        print(f"{n2}\t{wavelength_rydberg:.2f}\t\t{wavelength_bohr:.2f}")

def main():
    """
    Main function to calculate and display the wavelengths for the Pfund and Humphreys series.
    """
    pfund_n1 = 5
    humphreys_n1 = 6
    n2_range_pfund = range(pfund_n1 + 1, pfund_n1 + 6)
    n2_range_humphreys = range(humphreys_n1 + 1, humphreys_n1 + 6)
    
    print_wavelengths("Pfund", pfund_n1, n2_range_pfund)
    print()
    print_wavelengths("Humphreys", humphreys_n1, n2_range_humphreys)

if __name__ == "__main__":
    main()
