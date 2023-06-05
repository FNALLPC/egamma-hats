def make_ecal_deposit():
    from matplotlib.widgets import Slider,CheckButtons
    import numpy as np
    import matplotlib.pyplot as plt

    def makegrid(min_intensity_,ax):
        ax.cla()
        for i in range(10):
            for j in range(10):
                # Calculate the Euclidean distance from the central cell
                distance = np.sqrt((i - center_x)**2 + (j - center_y)**2)
        
                # Set the color intensity based on the distance
                color_intensity = 1 / (distance + 1)  # Adjust the denominator as needed
        
        
                # Apply the minimum intensity threshold
                if color_intensity < min_intensity_:
                    color_intensity = min_intensity_
                # Set the cell value based on the color intensity
                grid[i, j] = 1 - color_intensity

        # Plot the grid
        ax.imshow(grid, cmap='gray', origin='lower')
        ax.set_xticks(np.arange(10))
        ax.set_yticks(np.arange(10))
        ax.grid(color='gray', linewidth=0.5)

    fig = plt.figure()
    fig.subplots_adjust(bottom=0.3),fig.tight_layout()
    # Plot a histogram of the invariant mass distribution (should peak around 91 GeV)
    ax = fig.add_subplot(111)

    # Create a 5x5 grid of cells
    grid = np.zeros((10, 10))

    # Set the central cell coordinates
    center_x, center_y = 3, 3
    min_intensity=0.2
    # Iterate over each cell in the grid

    slider_ax = plt.axes([0.2, 0.1, 0.6, 0.03])
    slider = Slider(slider_ax, 'Min Threshold', 0.0, 1.0, valinit=min_intensity)

    makegrid(min_intensity,ax)

    def update_grid(val):
        min_intensity_=slider.val
        makegrid(min_intensity_,ax)
        fig.canvas.draw_idle()
    
    slider.on_changed(update_grid)

    fig.canvas.draw()