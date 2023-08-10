import numpy as np
import matplotlib.pyplot as plt
import pyvista as pv
import os

# Visualization function

def visualize(rho, x, y, u, v, x_min, x_max, y_min, y_max, step, freq, output_folder):
    plt.clf()
    cval = rho.flatten()
    plt.scatter(x, y, c=cval, cmap=plt.cm.autumn, s=20, alpha=0.5)
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f'SPH Simulation: 2D Dam Break Case (Step: {step})')
    # Add a colorbar to the plot
    cbar = plt.colorbar()
    cbar.set_label('Density')
    plt.pause(0.01)

    # Save a PNG image every freq time steps
    if step % freq == 0:
        plt.savefig(os.path.join(output_folder, f"sph{step:04d}.png"))


# Create a PyVista mesh from particle positions
def create_mesh(x, y,step, vtk_freq):
    if step % vtk_freq == 0:
        points = np.column_stack((x, y, np.zeros_like(x)))
        return pv.PolyData(points)

# Function to write data to a VTK file
def write_vtk_file(mesh, density, pressure, step, vtk_freq, output_folder):
    if step % vtk_freq == 0:
        mesh["Density"] = density
        mesh["Pressure"] = pressure
        vtk_file = os.path.join(output_folder, f"sph{step:03d}.vtk")
        # vtk_file = f"sph_results_{time_step:03d}.vtk"
        mesh.save(vtk_file)

