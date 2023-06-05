import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('default')

def plot_comparison_histogram(A, B, X, low, high, bin_size,sel=''):
    # Extract the desired columns from each DataFrame
    if sel:
        column_X_A = A.query(sel)[X]
        column_X_B = B.query(sel)[X]
    else:
        column_X_A = A[X]
        column_X_B = B[X]
    
    fig, ax = plt.subplots(figsize=(10,5))

    # Plot the data
    binning = np.arange(low, high + bin_size, bin_size)
    ax.hist(column_X_A, label="Good", bins=binning, weights=np.ones_like(column_X_A) / float(len(column_X_A)),histtype='step')
    ax.hist(column_X_B, label='Junk', bins=binning, weights=np.ones_like(column_X_B) / float(len(column_X_B)),histtype='step')

    # Add labels and title to the plot
    ax.set_xlabel(X)
    ax.set_ylabel('Photons')
    ax.set_title(f'Comparison of {X}')

    # Add a legend to differentiate between A and B
    ax.legend(loc='best')

    # Display the plot
    plt.show()
