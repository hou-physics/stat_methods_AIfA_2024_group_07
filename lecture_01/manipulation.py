import numpy as np

def sample_sphere(n):
    """
    Generates random spherical coordinates.

    Parameters:
    n (int): Number of spherical coordinates to generate.

    Returns:
    tuple: Two arrays containing 'n' randomly generated theta and phi values.
           Theta ranges from 0 to 2*pi radians, and phi ranges from 0 to pi radians.
    """
    
    theta = 2 * np.pi * np.random.rand(n)
    phi = np.arccos(2 * np.random.rand(n) - 1)

    return theta, phi

# -----------------------------------------------------------------------------------------------------------------------------

def get_cartesian_coords(phi, theta, r=1):
    """
    Converts spherical coordinates to Cartesian coordinates for a sphere of given radius.

    Parameters:
    phi (array-like): Array of azimuthal angles (radians).
    theta (array-like): Array of polar angles (radians).
    r (float, optional): Radius of the sphere. Defaults to 1.

    Returns:
    tuple: Three arrays containing the x, y, and z coordinates of the points in 3D space.
    """

    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)
    
    return x, y, z

# -----------------------------------------------------------------------------------------------------------------------------

# Following function directly returns the cartessian coordinates for 'n' randomly generated theta and phi values.

def make_sphere(n, r=1):
    """
    Generates random points on the surface of a sphere.

    Parameters:
    n (int): Number of points to generate.
    r (float, optional): Radius of the sphere. Defaults to 1.

    Returns:
    tuple: Three arrays containing the x, y, and z coordinates of 'n' points
           randomly distributed on the surface of a sphere with the given radius.
    """
    
    phi = np.arccos(2 * np.random.rand(n) - 1)  # Polar angle between 0 and pi
    theta = 2 * np.pi * np.random.rand(n)       # Azimuthal angle between 0 and 2*pi

    x = r * np.cos(theta) * np.sin(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(phi)

    return x, y, z
