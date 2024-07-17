# plot_unknown_wave.py

# This code was edited with the assistance of ChatGPT4o.

# This script analyzes a waveform from a CSV file, 
# identifies its primary frequency components, 
# and plots both the original and fitted waveforms. 
# The operation is: first, it reads time and waveform values 
# from a CSV file named `unknown_wave.csv`. 
# Then, it uses a Fourier transform to determine the primary 
# frequency components (α and β) of the waveform. 
# Finally, it plots the original waveform and generates a fitted waveform 
# using the identified frequency components for comparison.


from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.fft import fft, fftfreq

def load_waveform_data(file_path):
    """
    Load waveform data from a CSV file.

    Parameters:
    file_path (Path): Path to the CSV file containing waveform data.

    Returns:
    np.ndarray: Array of time values.
    np.ndarray: Array of waveform values.
    """
    data = pd.read_csv(file_path, header=None)
    data.columns = ['time', 'waveform']  # Assigning column names
    t = data['time'].values
    y = data['waveform'].values
    return t, y

def find_frequency_components(t, y):
    """
    Find the frequency components of a waveform using Fourier transform.

    Parameters:
    t (np.ndarray): Array of time values.
    y (np.ndarray): Array of waveform values.

    Returns:
    float: Frequency component alpha.
    float: Frequency component beta.
    """
    yf = fft(y)
    xf = fftfreq(len(t), (t[1] - t[0]) / (2.0 * np.pi))

    # Find the peaks in the Fourier transform (positive frequencies only)
    positive_freqs = xf[:len(xf)//2]
    positive_magnitudes = np.abs(yf[:len(yf)//2])

    # Find the indices of the highest peaks
    alpha_index = np.argmax(positive_magnitudes)
    beta_index = np.argmax(positive_magnitudes[1:]) + 1

    # Get the frequencies corresponding to the peaks
    alpha = positive_freqs[alpha_index]
    beta = positive_freqs[beta_index]

    return alpha, beta

def plot_waveforms(t, y, alpha, beta):
    """
    Plot the original and fitted waveforms.

    Parameters:
    t (np.ndarray): Array of time values.
    y (np.ndarray): Array of original waveform values.
    alpha (float): Frequency component alpha.
    beta (float): Frequency component beta.
    """
    # Plot the original data
    plt.figure(Path(__file__).name)
    plt.subplot(2, 1, 1)
    plt.title(f"QIS102 Task 13-03: Original Waveform")
    plt.plot(t, y, label='Original Data')
    plt.grid("on")
    plt.legend()

    # Generate the waveform using the determined alpha and beta
    y_fit = 2 * np.sin(alpha * t) * np.cos(beta * t)

    # Plot the fitted waveform
    plt.subplot(2, 1, 2)
    plt.title(f"Fitted Waveform: alpha = {alpha:.2f}, beta = {beta:.2f}")
    plt.plot(t, y_fit, linestyle='--')
    plt.grid("on")
    plt.legend()

    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to execute the waveform analysis and plotting.
    """
    # Load the data from the CSV file
    data_file = Path(__file__).parent / 'unknown_wave.csv'
    t, y = load_waveform_data(data_file)

    # Find the frequency components
    alpha, beta = find_frequency_components(t, y)
    print(f"Determined values: alpha = {alpha}, beta = {beta}")

    # Plot the waveforms
    plot_waveforms(t, y, alpha, beta)

if __name__ == "__main__":
    main()
