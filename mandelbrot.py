from math import sqrt
from stability import Stability

MAX_ITER = 50


def mandelbrot(c_x, c_y):
    x, y = 0, 0
    for _ in range(MAX_ITER):
        x_1, y_1 = (x**2 - y**2 + c_x), (2 * y * x + c_y)
        abs = sqrt(x_1**2 + y_1**2)
        if abs > 2.0:
            return Stability.Unstable
        x, y = x_1, y_1

    return Stability.Stable
