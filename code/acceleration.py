import numpy as np

def acceleration(m, x, y, u, v, rho, P, g, visc, h, grad_W_pre, lap_W_visc, neighbor_list):
    ''' Perform the sum of the pressure forces and viscous forces and gravity'''
    accel_x = np.zeros(len(x))
    accel_y = np.zeros(len(x))
    for i in range(len(x)):
        grav_x = 0.0
        grav_y = - g
        for j in neighbor_list[i]:
            if i==j:
                continue
            dx = x[i] - x[j]
            dy = y[i] - y[j]
            rij = np.sqrt(dx ** 2 + dy ** 2)

            v_rel_x = u[i] - u[j]
            v_rel_y = v[i] - v[j]

            # visc = 2 * alpha * h * c0 / (rho[i] + rho[j])

            gradWij = grad_W_pre(dx, dy , h)

            # grad_P_x = -(P[i] / (rho[i] ** 2) + P[j] / (rho[j] ** 2)) * gradWij[0]
            # grad_P_y = -(P[i] / (rho[i] ** 2) + P[j] / (rho[j] ** 2)) * gradWij[1]

            grad_P_x =  m * (P[i] + P[j]) * gradWij[0] / (2 * rho[i] * rho[j])
            grad_P_y =  m * (P[i] + P[j]) * gradWij[1] / (2 * rho[i] * rho[j])

            visc_x = m * visc * (u[j]-u[i]) * lap_W_visc(rij, h) / (rho[i]*rho[j])
            visc_y = m * visc * (v[j]-v[i]) * lap_W_visc(rij, h) / (rho[i]*rho[j])

            accel_x[i] +=  (grad_P_x + visc_x)
            accel_y[i] +=  (grad_P_y + visc_y)

        accel_x[i] +=  grav_x
        accel_y[i] +=  grav_y
    return accel_x, accel_y
