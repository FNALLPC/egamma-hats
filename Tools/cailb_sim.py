# Import libraries
import numpy as np
import matplotlib.pyplot as plt


def generate_random_numbers(x0, gamma, n):
    """Generate random numbers from Breit-Wigner distribution"""
    # Generate uniform random numbers between 0 and 1
    uniform_numbers = np.random.uniform(0, 1, n)

    # Transform uniform numbers to Breit-Wigner distribution
    breit_wigner_numbers = np.tan(np.pi * (uniform_numbers - 0.5))

    # Scale and shift the numbers to match desired x0 and gamma values
    breit_wigner_numbers = x0 + gamma * breit_wigner_numbers

    return breit_wigner_numbers


# Define a function to generate electron pairs with a realistic invariant mass
def generate_electron_pairs_with_mass(n, mean=91, std=2.5):
    # Set the seed for reproducibility
    np.random.seed(42)
    # Generate random m_ee values from a normal distribution with given mean and std
    # m_ee = np.random.normal(mean, std, n)
    m_ee = generate_random_numbers(mean, std, n)
    # Convert m_ee from GeV to MeV
    m_ee = m_ee * 1000
    # Generate random eta values between -5 and 5
    eta1 = np.random.uniform(-5, 5, n)
    eta2 = np.random.uniform(-5, 5, n)
    # Generate random phi values between 0 and 2*pi
    phi1 = np.random.uniform(0, 2 * np.pi, n)
    phi2 = np.random.uniform(0, 2 * np.pi, n)
    # Calculate the pT values using the inverse of the formula for the invariant mass
    pT1 = np.sqrt(m_ee**2 / (2 * (np.cosh(eta1 - eta2) - np.cos(phi1 - phi2))))
    pT2 = pT1  # The pT values are equal by symmetry
    # Return a tuple of arrays
    return (pT1, pT2, eta1, eta2, phi1, phi2)


# Define a function to calculate the di-electron invariant mass
def calculate_invariant_mass(pT1, pT2, eta1, eta2, phi1, phi2):
    # Convert pT from GeV to MeV
    pT1 = pT1
    pT2 = pT2
    # Calculate the invariant mass using the formula
    m_ee = np.sqrt(2 * pT1 * pT2 * (np.cosh(eta1 - eta2) - np.cos(phi1 - phi2)))
    # Return the invariant mass array
    return m_ee


def reco_electron_pairs(
    pT1, pT2, eta1, eta2, phi1, phi2, calib, laser_corrections_scenario=2
):
    recopT1 = pT1 * (calib - 0.05)
    recopT2 = pT2 * (calib - 0.05)

    if laser_corrections_scenario == 2:
        recoeta1 = eta1
        recoeta2 = eta2

    if laser_corrections_scenario == 1:
        recoeta1 = eta1 * (calib - 0.03)
        recoeta2 = eta2 * (calib - 0.03)

    recophi1 = phi1
    recophi2 = phi2

    return recopT1, recopT2, recoeta1, recoeta2, recophi1, recophi2


def make_mass_plot(
    gen_m_ee,
    reco_m_ee,
    alpha_Calib,
    laser_scenario,
    pT1,
    pT2,
    eta1,
    eta2,
    phi1,
    phi2,
    xlim=[60, 120],
    ylim=[0, 6000],
    bin_width=0.5,
):
    # from matplotlib.widgets import Slider  # Import Slider class

    ################################################################
    def plotz(ax, gen_m_ee, reco_m_ee):
        hist = ax.hist(
            [gen_m_ee / 1000, reco_m_ee / 1000],
            histtype="step",
            linewidth=2,
            bins=np.arange(xlim[0], xlim[1] + bin_width, bin_width).tolist(),
            label=["generated electron pairs", "reconstructed electron pairs"],
        )  # Divide by 1000 to convert from MeV to GeV
        ax.set_xlabel("Invariant mass (GeV)")
        ax.set_ylabel("Counts")
        ax.set_xlim((xlim[0], xlim[1]))
        ax.set_ylim((ylim[0], ylim[1]))
        ax.set_title("Dielectron invariant mass distribution")
        ax.legend()

    ################################################################
    # Create a figure and adjust its size and position
    fig = plt.figure()
    fig.subplots_adjust(bottom=0.3), fig.tight_layout()
    # Plot a histogram of the invariant mass distribution (should peak around 91 GeV)
    ax = fig.add_subplot(111)
    plotz(ax, gen_m_ee, reco_m_ee)
    # Create a new axes for the sliders below the plot
    slider_ax = fig.add_axes(
        [0.3, 0.05, 0.5, 0.03]
    )  # Position and size of the slider axes
    slider_ax_2 = fig.add_axes(
        [0.3, 0.1, 0.5, 0.03]
    )  # Position and size of the slider axes
    #calib_slider = Slider(slider_ax, "alpha_Calib", 0.9, 1.2, valinit=alpha_Calib)
    #scenario_slider = Slider(
    #    slider_ax_2, "laser scenario", 0, 2, valinit=laser_scenario, valstep=1
    #)

    ################################################################
    # Define a function that will update the plot when the slider value changes
    def update(val):
        # Get the new value of calib from the slider
        calib = 1 #calib_slider.val
        scenario = 1 #scenario_slider.val
        # Update recopT1 and recopT2 using the new calib value
        recopT1, recopT2, recoeta1, recoeta2, recophi1, recophi2 = reco_electron_pairs(
            pT1, pT2, eta1, eta2, phi1, phi2, calib, scenario
        )
        # Recalculate reco_m_ee using the updated recopT1 and recopT2
        reco_m_ee = calculate_invariant_mass(
            recopT1, recopT2, recoeta1, recoeta2, recophi1, recophi2
        )
        # Clear the previous histogram data
        ax.cla()
        # Plot a new histogram with the updated reco_m_ee data
        plotz(ax, gen_m_ee, reco_m_ee)
        # Redraw the figure
        fig.canvas.draw_idle()

    ################################################################
    # Register the update function with the slider object
    # scenario_slider.on_changed(update)
    # calib_slider.on_changed(update)

    fig.canvas.draw()
    ################################################################
