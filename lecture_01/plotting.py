import matplotlib.pyplot as plt

def sphere(x, y, z):

    """
    Creates a 3D scatter plot of points in spherical coordinates.

    Parameters:
    x (array-like): Array of x-coordinates.
    y (array-like): Array of y-coordinates.
    z (array-like): Array of z-coordinates.

    Returns:
    plotly.graph_objects.Figure: A 3D scatter plot displaying the points in spherical coordinates.
    """

    # Create a 3D scatter plot
    fig = plt.figure(figsize = (10, 8))
    ax = fig.add_subplot(projection='3d')
    ax.scatter(x, y, z, s = 2, color = 'teal', alpha = 0.7)

    # Set axis labels and plot title
    ax.set_xlabel('X values')
    ax.set_ylabel('Y values')
    ax.set_zlabel('Z values')
    ax.set_aspect('auto')

    plt.show()

# -----------------------------------------------------------------------------------------------------------------------------

def projection(x, y, z):

    """
    Creates a subplot containing projections of points along different axes.

    Parameters:
    x (array-like): Array of x-coordinates.
    y (array-like): Array of y-coordinates.
    z (array-like): Array of z-coordinates.

    Returns:
    plotly.graph_objects.Figure: A subplot containing projections of points along x, y, and z axes.
    """

    # Create subplots with 1 row and 3 columns
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize = (18, 8))

    ax1.scatter(x, y, s = 2, c = 'teal', alpha = 0.7)
    ax1.set_title('XY Plane')
    ax1.set_aspect('auto')

    ax2.scatter(y, z, s = 2, c = 'crimson', alpha = 0.7)
    ax2.set_title('YZ Plane')
    ax2.set_aspect('auto')

    ax3.scatter(z, x, s = 2, c = '#ff4500', alpha = 0.5)
    ax3.set_title('ZX Plane')
    ax3.set_aspect('auto')

    plt.tight_layout()
    plt.show()

# -----------------------------------------------------------------------------------------------------------------------------

def histogram(x, y, z):
    
    """
    Creates a subplot containing histograms of points along x, y, and z axes.

    Parameters:
    x (array-like): Array of x-coordinates.
    y (array-like): Array of y-coordinates.
    z (array-like): Array of z-coordinates.

    Returns:
    plotly.graph_objects.Figure: A subplot containing histograms of points along x, y, and z axes.
    """

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize = (18, 4))

    ax1.hist(x, bins = 55, edgecolor = 'black', color = 'teal', alpha = 0.7, lw = 0.5)
    ax1.set_title('X Distribution')

    ax2.hist(y, bins = 55, edgecolor = 'black', color = 'crimson', alpha = 0.7, lw = 0.5)
    ax2.set_title('Y Distribution')

    ax3.hist(z, bins = 55, edgecolor = 'black', color = '#ff4500', alpha = 0.7, lw = 0.5)
    ax3.set_title('Z Distribution')

    plt.tight_layout()
    plt.show()

# -----------------------------------------------------------------------------------------------------------------------------
