import numpy as np

# SPH Interpolation kernel (Muller et al. 2003)
def W(r, h):
    """ Poly6 smoothing kernel """
    if 0 <= r <= h:
        return 315.0 / (64.0 * np.pi * h**9) * (h**2 - r**2)**3
    return 0.0

# SPH Gradient of interpolation kernel
def grad_W(x, y, h):
    """ Gradient of Poly6 smoothing kernel """
    r = np.sqrt(x ** 2 + y ** 2)
    if 0 < r <= h:
        return np.array([-945.0 / (32.0 * np.pi * h**9) * x * (h**2 - r**2)**2,
                         -945.0 / (32.0 * np.pi * h**9) * y * (h**2 - r**2)**2,])
    return np.array([0.0, 0.0])

# SPH Gradient of interpolation kernel for pressure
def grad_W_pre(x, y, h):
    """ Gradient of spiky smoothing kernel """
    r = np.sqrt(x ** 2 + y ** 2)
    if 0 < r <= h:
        return np.array([-45.0 / (np.pi * h**6 * r) * x * (h - r)**2,
                         -45.0 / (np.pi * h**6 * r) * y * (h - r)**2,])
    return np.array([0.0, 0.0])

# SPH Laplacian of interpolation kernel
def lap_W(r, h):
    """ Laplacian of Poly6 smoothing kernel """
    if 0 < r <= h:
        return - 945.0 / (32.0 * np.pi * h**9) * (h**2 - r**2) * (3 * h**2 - 7 * r**2)
    return 0.0

# SPH Laplacian of interpolation kernel for visc
def lap_W_visc(r, h):
    """ Laplacian of spiky smoothing kernel """
    if 0 < r <= h:
        return  45.0 / (np.pi * h**6) * (h - r)
    return 0.0
