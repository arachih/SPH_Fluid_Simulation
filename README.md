# Smoothed Particle Hydrodynamics (SPH) Simulation

This is a Python implementation of a 2D Smoothed Particle Hydrodynamics (SPH) simulation for simulating fluid behavior in a dam break scenario.

## Overview

This simulation uses the SPH method to model fluid behavior in a 2D domain. It includes parameters for particle properties, domain dimensions, time step, and other simulation-specific settings.

## Dependencies

Make sure you have the following Python libraries installed:

- `numpy`
- `matplotlib`
- `pyvista`

pyvista is used to get vtk outputs to visualize flow using ParaView for example.

You can install them using the following command:

```
pip install numpy matplotlib pyvista
```
## Usage

1. Clone this repository:

```
git clone https://github.com/arachih/SPH_Fluid_Simulation.git
cd SPH_Fluid_Simulation/code
```

2. Run the simulation by executing the Python script:

```
python sph.py
```

## Other Python Files

Here's a brief description of the other Python files included in this simulation:

`acceleration.py` :

This module (`acceleration.py`) contains functions that compute the acceleration of particles based on various forces and interactions. It takes into account the gravitational force, pressure gradients, and artificial viscosity to update the acceleration components for each particle.

`boundary_conditions.py` :

The `boundary_conditions.py` file defines functions responsible for handling boundary conditions. It ensures that particles interacting with boundaries, such as walls, undergo inelastic collisions and are reflected or projected appropriately to maintain the integrity of the simulation.

`density_pressure.py` :

In the `density_pressure.py` module, you'll find functions related to calculating particle density and pressure. It employs the SPH method to estimate density based on the neighboring particles' contribution and uses the equation of state (EOS) to compute the corresponding pressure.

`euler.py` :

The `euler.py` file implements the Euler time integration scheme. It updates the velocity and position of particles based on the calculated acceleration. This scheme is utilized to advance the simulation in discrete time steps.

`hash_function.py` :

The `hash_function.py` module provides the HashFunction class, which implements spatial hashing techniques. It assists in efficiently finding neighbors of particles within given cells, optimizing the neighbor search process and overall simulation performance.

`post.py` :

The `post.py` module handles post-processing tasks for the simulation results. It generates PNG images to visualize the particle distribution and also produces VTK files for further analysis using visualization tools like Paraview.


## Parameters

- `N`: Number of particles
- `h`: Smoothing length
- `edge`: Limit of the walls
- `width`: Domain width
- `height`: Domain height
- `m`: Particle mass
- `rho0`: Reference density
- `c0`: Speed of sound
- `alpha`: Viscosity coefficient
- `gamma`: Tait equation gamma
- `dt`: Time step
- `k`: Coefficient of EOS
- `g`: Gravity acceleration
- `final_time`: Final simulation time
- `frequency`: Output frequency for images
- `vtk_freq`: Output frequency for VTK files
- `visc`: Artificial viscosity
- `eps`: Epsilon value
- `bdry_reflec`: Reflection coefficient for inelastic collision with boundaries
- `bdry_proj_dist`: Distance to push particles away from boundaries

## Visualization

The simulation results can be visualized using the generated images and VTK files in the `output` folder.
Here are visualizations of the simulation results using python and ParaView with Delaunay 2D filter

![til](./figs/sph.gif)
![til](./figs/sph_para.gif)

## Visualization Using ParaView (Version 5.9.0)

`paraview_visu_script.py` demonstrates the visualization setup for the generated Smoothed Particle Hydrodynamics (SPH) simulation results using ParaView version 5.9.0. The script utilizes ParaView's Python scripting capabilities to create and configure visualization elements, including loading VTK files, applying color maps, adjusting camera views, creating scalar bars, and generating animation frames. The resulting animation frames are saved as PNG images for further analysis and presentation. This script helps users reproduce and customize the visualization of SPH simulation results using ParaView's powerful visualization capabilities.

## Acknowledgments

- The code structure and concepts are inspired by the article "Particle-Based Fluid Simulation for Interactive Applications" by Müller & al (included in the repo)

## License

This project is licensed under the MIT License 

---

