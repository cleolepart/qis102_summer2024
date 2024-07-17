# square_wave.py

from pathlib import Path

import py_compile


import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator
from numpy.fft import fft, ifft


def plot_samples(ax, ts, ys):
    num_samples = ts.size
    ax.plot(ts, ys, color="lightgray", linewidth=1)
    ax.scatter(ts, ys, color="black", marker=".", s=10.0, zorder=2)
    ax.set_title(f"Sampled Wave ({num_samples} samples)")
    ax.set_xlabel("scaled time", loc="right")
    ax.set_ylabel("amplitude")


def plot_dft(ax, ct):
    num_terms = 40

    # fmt: off
    ax.bar(range(0, num_terms), ct.real[:num_terms],
        color="blue", label="cosine", zorder=2)
    ax.bar(range(0, num_terms), -ct.imag[:num_terms],
        color="red",  label="sine", zorder=2)    
    # fmt: on

    ax.grid(which="major", axis="x", color="black", linewidth=1)
    ax.grid(which="minor", axis="x", color="lightgray", linewidth=1)
    ax.grid(which="major", axis="y", color="black", linewidth=1)
    ax.grid(which="minor", axis="y", color="lightgray", linewidth=1)

    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.set_title("Fast Fourier Transform")
    ax.set_xlabel("frequency", loc="right")
    ax.set_ylabel("amplitude")
    ax.legend(loc="upper right")


def plot_idft(ax, ts, yr):
    num_samples = ts.size
    ax.plot(ts, yr, color="purple")
    ax.set_title(f"Inverse FFT ({num_samples} samples)")
    ax.set_xlabel("scaled time", loc="right")
    ax.set_ylabel("amplitude")


def plot_power_spectrum(ax, ct):
    num_terms = 40
    ax.bar(
        range(0, num_terms), abs(ct[:num_terms]), color="green", label="sine", zorder=2
    )
    ax.grid(which="major", axis="x", color="black", linewidth=1)
    ax.grid(which="minor", axis="x", color="lightgray", linewidth=1)
    ax.grid(which="major", axis="y", color="black", linewidth=1)
    ax.grid(which="minor", axis="y", color="lightgray", linewidth=1)

    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.set_title("Power Spectrum")
    ax.set_xlabel("frequency", loc="right")
    ax.set_ylabel(r"$\Vert amplitude \Vert$")


def main(file_name):
    file_path = Path(__file__).parent / file_name
    samples = np.genfromtxt(file_path, delimiter=",")
    ts, ys = samples.T

    ct = 2 / len(ys) * fft(ys)
    yr = len(ys) / 2 * ifft(ct)
    ct[0] /= 2  # DC value should NOT be doubled

    plt.figure(
        Path(__file__).name + f" ({file_name})",
        figsize=(12, 8),
    )

    plot_samples(plt.subplot(2, 2, 1), ts, ys)
    plot_dft(plt.subplot(2, 2, 2), ct)
    plot_idft(plt.subplot(2, 2, 3), ts, np.real(yr))
    plot_power_spectrum(plt.subplot(2, 2, 4), ct)

    plt.tight_layout()
    plt.show()


file_name = "samples_square.csv"
main(file_name)

"""
1. Why does the power spectrum of the sampled waveform have so many frequencies?

The power spectrum of the sampled waveform has so many frequencies because a 
square wave is composed of a fundamental frequency and its harmonics. 
The sharp transitions of a square wave introduce high-frequency components, 
which means its Fourier series contains an infinite number of odd harmonics. 
This results in a power spectrum that shows many distinct frequency components, 
each corresponding to these harmonics. (source: https://en.wikipedia.org/wiki/Spectral_density)

2. Why does the magnitude of the DC component equal 1/2?

The magnitude of the DC component equals 1/2 because 
the DC component represents the average value of the waveform 
over its period. For a square wave that has an amplitude of 1 
over half the period and 0 over the other half, the average value is 0.5. 
This is calculated by taking the integral of the waveform over one period 
and dividing by the period length, resulting in 1/2. (source: Arfken & Weber, Mathematical Methods for Physicists, 6th ed., 2005, OUP)

3. Why are there no sine components in its DFT?

There are no sine components in its Discrete Fourier Transform (DFT) 
because the square wave is symmetric around its midpoint (an even function). 
In Fourier analysis, even functions are represented only by cosine terms, 
while odd functions are represented by sine terms. (source: Horowitz & Hill, The Art of Electronics, 3rd Ed., 2015, MIT Press)
"""
