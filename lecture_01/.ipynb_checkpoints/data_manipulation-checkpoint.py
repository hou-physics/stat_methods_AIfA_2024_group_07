import numpy as np

def sample_sphere(n):
    """
    Docstring goes here...
    """
    # Set a random seed for reproducibility
    np.random.seed(0)

    # Generate 10,000 points uniformly distributed on the unit sphere
    cos_theta = np.random.uniform(-1, 1, n)
    phi = np.random.uniform(0, 2 * np.pi, n)
    theta = np.arccos(cos_theta)
    return theta, phi

def get_cartesian_coords(theta, phi, r = 1):
    """
    Docstring goes here...
    """
    # Convert spherical coordinates to Cartesian coordinates
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)
    return x, y, z



