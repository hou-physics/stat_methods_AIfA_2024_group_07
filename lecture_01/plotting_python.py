import matplotlib.pyplot as plt

def plotting(x, y, z):
    # Plot 2D scatter plots for projections
    fig, axs = plt.subplots(1, 3, figsize=(18, 5))

    axs[0].scatter(y, z, s=1, alpha=0.5)
    axs[0].set_xlabel('y')
    axs[0].set_ylabel('z')
    axs[0].set_title('Projection along x-axis (YZ plane)')

    axs[1].scatter(x, z, s=1, alpha=0.5, color='orange')
    axs[1].set_xlabel('x')
    axs[1].set_ylabel('z')
    axs[1].set_title('Projection along y-axis (XZ plane)')

    axs[2].scatter(x, y, s=1, alpha=0.5, color='green')
    axs[2].set_xlabel('x')
    axs[2].set_ylabel('y')
    axs[2].set_title('Projection along z-axis (XY plane)')

    plt.tight_layout()
    plt.show()

    # Plot histograms for x, y, z distributions
    fig, axs = plt.subplots(1, 3, figsize=(18, 5))
    bins = 50

    axs[0].hist(x, bins=bins, color='blue', alpha=0.7, edgecolor='black')
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('Frequency')
    axs[0].set_title('Histogram of x')

    axs[1].hist(y, bins=bins, color='orange', alpha=0.7, edgecolor='black')
    axs[1].set_xlabel('y')
    axs[1].set_ylabel('Frequency')
    axs[1].set_title('Histogram of y')

    axs[2].hist(z, bins=bins, color='green', alpha=0.7, edgecolor='black')
    axs[2].set_xlabel('z')
    axs[2].set_ylabel('Frequency')
    axs[2].set_title('Histogram of z')

    plt.tight_layout()
    plt.show()