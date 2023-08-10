import numpy as np

# Calculate density at each particle
def calculate_density(m, W, x, y, h, neighbor_list):
    density = np.zeros(len(x))
    for i in range(len(x)):
        for j in neighbor_list[i]:
            r = np.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)
            density[i] += m * W(r, h)
    return density

# Calculate pressure using Tait equation
def calculate_pressure(c0, gamma, rho, rho0):
    return (c0 ** 2 * rho0 / gamma)* ((rho / rho0) ** gamma - 1.0)

# Calculate pressure using Equation of State
def calculate_pressure_eos(k, rho, rho0):
    return k * (rho - rho0)
