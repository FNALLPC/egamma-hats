def gen_data_exp():
    import numpy as np

    # Generate simulated data
    np.random.seed(0)  # For reproducibility

    # Constants
    true_slope = 0.5
    true_intercept = 2.0
    true_sigma = 0.5

    # Generate true energy values
    energy_true = np.random.uniform(10, 100, 100)

    # Generate measured energy values with noise
    energy_measured = (
        true_slope * energy_true
        + true_intercept
        + (
            np.random.normal(0, true_sigma * 1.6, 100)
            * np.random.normal(0, true_sigma, 100)
            * energy_true
        )
    )

    return energy_true, energy_measured


def gen_data_nice():
    import numpy as np

    # Generate simulated data
    np.random.seed(0)  # For reproducibility

    # Constants
    true_slope = 0.5
    true_intercept = 2.0
    true_sigma = 0.5

    # Generate true energy values
    energy_true = np.random.uniform(10, 100, 100)

    # Generate measured energy values with noise
    energy_measured = (
        true_slope * energy_true
        + true_intercept
        + (np.random.normal(0, true_sigma * 1.9, 100))
    )
    return energy_true, energy_measured
