"""
Smoothed Particle Hydrodynamics (SPH) Simulation
Author: Azeddine RACHIH
Date: 10th August 2023
"""

import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib.animation import FuncAnimation
from matplotlib.animation import PillowWriter
import itertools
import time
import pyvista as pv
import smoothing_kernels as sk
from hash_function import HashFunction
import boundary_conditions
import density_pressure
import euler
import acceleration as acc
import post as ps


# Parameters
N = 1200        # Number of particles
h = 5          # Smoothing length
edge = 5       # limit of the walls
width = 400    # domaine width
height = 400   # height width
m = 1.         # Particle mass
rho0 = 1.      # Reference density
c0 = 10.0      # Speed of sound
alpha = 1.     # Viscsity coefficient
gamma = 7.0    # Tait equation gamma
dt = 0.05       # Time step
k = 20         # Coefficient of EOS
g = 0.2        # Gravity acceleration
final_time = 10000 # Final simulation time
frequency = 50 # output frequency images
vtk_freq = 50  # output frequency VTK
visc = 0.5        # Artificial viscosity
eps = 0.1       # original eps=0.1
bdry_reflec = 0.5  # 50% reflection coefficient for inelastic collision
bdry_proj_dist = 0.0  # Distance to push the particle away from the boundary
total_steps = int(final_time / dt)

# Square boundary
x_min, y_min = edge , edge
x_max, y_max = width - edge , height - edge

# Sub-square initial confinement
x_sub_min, x_sub_max = x_min , int((x_max - x_min) * 0.25)
y_sub_min, y_sub_max = y_min , y_max - 1

x = np.zeros(N)
y = np.zeros(N)

# set-up a dam-break scenario
if N > ((y_sub_max - y_sub_min) // h) * ((x_sub_max - x_sub_min) // h):
    raise ValueError("reduce the number of points (n) or reduce the kernel radius (h)")

i=0
np.random.seed(42)
for yi in np.arange(y_sub_min, y_sub_max, h):
    for xi in np.arange(x_sub_min, x_sub_max, h):
        if i < N:
            x[i],y[i] = xi + np.random.uniform(0, h * eps), yi + np.random.uniform(0, h * eps)
        i += 1
    pass

u = np.zeros(N)
v = np.zeros(N)
accel_x = np.zeros(N)
accel_y = np.zeros(N)
rho = np.zeros(N)
P = np.zeros(N)

# Create a folder to store output files
output_folder = "output"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Record the start time
start_time = time.time()

# Initialize Hash Function
hash_function = HashFunction(x_min, x_max, y_min, y_max, h)

# Main simulation loop
for step in range(total_steps):

    hash_function.assign_particles_to_cells(x, y)
    neighbor_list = hash_function.find_neighbors(x, y)

    rho = density_pressure.calculate_density(m, sk.W, x, y, h, neighbor_list)
    P = density_pressure.calculate_pressure_eos(k, rho, rho0)

    accel_x, accel_y = acc.acceleration(m, x, y, u, v, rho, P, g, visc,h, sk.grad_W_pre, sk.lap_W_visc, neighbor_list)

    euler.euler(x, y, u, v, dt, accel_x, accel_y)
    boundary_conditions.apply_bc(x, y, u, v, x_min, x_max, y_min, y_max, bdry_reflec, bdry_proj_dist)

    # Visualize the results
    ps.visualize(rho, x, y, u, v, x_min, x_max, y_min, y_max, step, frequency, output_folder)

    # Save data to VTK files every k time steps
    mesh = ps.create_mesh(x, y, step, vtk_freq)
    ps.write_vtk_file(mesh, rho, P, step, vtk_freq, output_folder)

# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time
print(f"Elapsed Time: {elapsed_time:.6f} seconds")
plt.show()

