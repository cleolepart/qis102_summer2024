# uncertainty_principle.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def f(x):
    # The Gaussian standard normal probability density function
    return (
        1
        / (sigma * np.sqrt(2 * np.pi))
        * np.exp((-1 / 2) * np.power(x, 2) / (np.power(sigma, 2)))
    )


def plot_samples(ts, ys, ax):
    global wave_pdf
    (wave_pdf,) = ax.plot(ts, ys, animated=True)
    ax.set_title("Particle Location (Probability Density)")
    ax.set_xlabel("Distance", loc="right")
    ax.set_ylabel("Probability Density")
    ax.set_ylim(0, 25)


def plot_powerspec(ps, ax):
    global wave_ps
    (wave_ps,) = ax.plot(range(len(ps)), ps, color="green", animated=True)
    ax.set_title("Particle Frequencies")
    ax.set_xlabel("Frequency", loc="right")
    ax.set_ylabel(r"$\Vert Amplitude\Vert$")
    ax.set_ylim(0, 1)


def anim_frame_counter():
    global sigma
    n = 1
    while n < 1200:
        sigma = 10 / n if n <= 600 else 10 / (1200 - n)
        n += 1
        yield n


def anim_draw_frame(t):
    global sigma
    ys = f(ts)
    wave_pdf.set_data(ts, ys)

    sigma /= 30
    ys = f(ts)
    ca = np.fft.rfft(ys) / 2
    ps = np.abs(ca) / len(ca)

    wave_ps.set_data(range(len(ps)), ps)

    return (
        wave_pdf,
        wave_ps,
    )


def main():
    global ts, sigma, anim

    ts = np.linspace(-1, 1, 1000, endpoint=False)

    sigma = 1
    ys = f(ts)

    ca = np.fft.rfft(ys) / 2
    ps = np.abs(ca) / len(ca)

    plt.figure(Path(__file__).name, figsize=(12, 4))

    ax_pdf = plt.subplot(1, 2, 1)
    ax_ps = plt.subplot(1, 2, 2)

    plot_samples(ts, ys, ax_pdf)
    plot_powerspec(ps, ax_ps)

    # fmt: off
    anim = FuncAnimation(ax_pdf.figure,
        anim_draw_frame, anim_frame_counter, interval=25,
        cache_frame_data=False, blit=True, repeat=False)
    # fmt: on

    plt.tight_layout()
    plt.show()


main()

"""
1. Why do the Fourier Transform frequencies spread out as we more tightly confine where the particle is likely to be found?
   - The spreading out of Fourier Transform frequencies as the particle's position is more tightly confined is a manifestation 
   of the uncertainty principle. According to this principle, there is an inverse relationship between the uncertainty in position (Δx) 
   and the uncertainty in momentum (Δp). When the particle's position is more precisely determined (Δx decreases), 
   the uncertainty in its momentum increases (Δp increases), resulting in a wider spread of frequencies in the Fourier Transform, 
   as these frequencies correspond to the possible momentum values of the particle.

2. At the end of the animation, when the Power Spectrum shows only one frequency, why does the probability of finding the particle at any point $x$ spread out infinitely?
   - When the Power Spectrum shows only one frequency, it indicates that the particle has a well-defined momentum with zero uncertainty. According to the uncertainty principle, 
   if the momentum is precisely known (Δp = 0), the uncertainty in position (Δx) becomes infinite. This means that the particle's position is completely undetermined 
   and can be found anywhere in space with equal probability, leading to an infinitely spread-out probability density function.

3. Do you believe a particle with 100% exactly known momentum could potentially exist anywhere in the universe - why or why not?
    - No, a particle with 100% exactly known momentum cannot exist in our universe because of the inherent constraints imposed 
    by the uncertainty principle. Knowing both the exact position and momentum of a quantum particle would violate the fundamental 
    principles of quantum mechanics. This would either imply we are in a different universe with different physical laws or 
    that our definition of "exact" allows for a margin of error much larger than Planck’s constant. In our universe, 
    where quantum mechanics holds, such a scenario is impossible. If it were possible, it would mean that atoms and the structures 
    dependent on quantum mechanics couldn't exist, leading to a drastically different and likely uninhabitable universe.

    (source 1-3: Griffiths, Introduction to Quantum Mechanics, 3rd Ed., 2018, Cambridge)
"""

