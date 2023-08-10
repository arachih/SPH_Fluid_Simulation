def apply_bc(x, y, u, v, x_min, x_max, y_min, y_max, bdry_reflec, bdry_proj_dist):
# def apply_bc(N, x_min, x_max, y_min, y_max, bdry_reflec, bdry_proj_dist):
    '''Apply boundary conditions with inelastic collisions'''
    for i in range(len(x)):
        if x[i] < x_min:
            u[i] *= - bdry_reflec
            x[i] = x_min
            x[i] += bdry_proj_dist
        elif x[i] > x_max:
            u[i] *= - bdry_reflec
            x[i] = x_max
            x[i] -= bdry_proj_dist

        if y[i] < y_min:
            v[i] *= - bdry_reflec
            y[i] = y_min
            y[i] += bdry_proj_dist
        elif y[i] > y_max:
            v[i] *= - bdry_reflec
            y[i] = y_max
            y[i] -= bdry_proj_dist
