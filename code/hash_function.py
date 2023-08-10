import numpy as np

# Find neighbors using the grid
class HashFunction:
    def __init__(self, x_min, x_max, y_min, y_max, cell_size):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.cell_size = cell_size
        self.nx = int(np.ceil((x_max - x_min) / cell_size))
        self.ny = int(np.ceil((y_max - y_min) / cell_size))
        self.grid = [[] for _ in range(self.nx * self.ny)]

    def assign_particles_to_cells(self, x, y):
        # Assign particles to cells using grid logic
        self.grid = [[] for _ in range(self.nx * self.ny)]
        for i in range(len(x)):
            cx = int(np.clip((x[i] - self.x_min) / self.cell_size, 0, self.nx - 1))
            cy = int(np.clip((y[i] - self.y_min) / self.cell_size, 0, self.ny - 1))
            cell_index = cx + cy * self.nx
            # print(cx, cy,cell_index)
            self.grid[cell_index].append(i)

    def find_neighbors(self, x, y):
        # Find neighbors using assigned cells and grid logic
        neighbor_list = [[] for _ in range(len(x))]
        # print(self.grid)
        for i in range(len(x)):
            cx = int(np.clip((x[i] - self.x_min) / self.cell_size, 0, self.nx - 1))
            cy = int(np.clip((y[i] - self.y_min) / self.cell_size, 0, self.ny - 1))
            # current_cell_index = cx + cy * self.nx
            for dxi in [-1, 0, 1]:
                for dyi in [-1, 0, 1]:
                    nx_idx = int(np.clip(cx + dxi, 0, self.nx - 1))
                    ny_idx = int(np.clip(cy + dyi, 0, self.ny - 1))
                    cell_index = nx_idx + ny_idx * self.nx
                    # if cell_index == current_cell_index:
                    #     # Skip adding neighbors from the same cell
                    #     continue
                    for j in self.grid[cell_index]:
                        dx = x[i] - x[j]
                        dy = y[i] - y[j]
                        rij = np.sqrt(dx ** 2 + dy ** 2)
                        if rij <= self.cell_size:
                            neighbor_list[i].append(j)
        return neighbor_list