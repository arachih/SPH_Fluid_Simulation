# Explicit time integration using euler scheme
def euler(x, y, u, v, dt, accel_x, accel_y):

    # Update velocity
    u += dt  * accel_x
    v += dt  * accel_y

    # Update position
    x += dt * u
    y += dt * v

