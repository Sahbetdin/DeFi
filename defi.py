from typing import Callable, List

#defi params
a1 = 3
b1 = 166

b2 = 724
c2 = 766

c3 = 10
d3 = 1

d4 = 1722
e4 = 2846

e5 = 22_500
a5 = 4_360
p = 0.3/100

#serving params:
da_initial_offset = 0.001
n_points = 30 # number of segments for solver
eps = 1.e-5 #threshold used for solver

def calc_out(x, y, dx):
    return y * dx / (x + dx) - p * dx

def calc_pipe(da):
    db = calc_out(a1, b1, da)
    dc = calc_out(b2, c2, db)
    dd = calc_out(c3, d3, dc)
    de = calc_out(d4, e4, dd)
    da1 = calc_out(e5, a5, de)
    return da1

def linspace(left: float, right: float, n: int):
    """
    equally distributed points on a line segment
    totally n segments, i.e. n+1 points.
    x1 and x2 are included.
    """
    d = (right - left) / n
    points = [None] * (n + 1)
    for i in range(n + 1):
        points[i] = left + d * i
    return points

def get_function_values(f: Callable, points: List[float]):
    values = [None] * len(points)
    for i, x in enumerate(points):
        values[i] = f(x) - x
        # print(i, points[i], x, values[i])
    return values

def get_index_max_value(values: List[float]):
    i_max = 0
    x_max = values[0]
    for i, el in enumerate(values):
        if el > x_max:
            x_max = el
            i_max = i
    return i_max

def get_new_left_right_points(i_max: int, points: List[float]) -> (float, float):
    assert i_max >= 0, "Be sure the passed index is non-negative"
    if i_max > 0:
        left = points[i_max - 1]
    else: #i_max == 0
        left = points[0]
    right = points[i_max + 1]
    return left, right


def solver(f: Callable, left: float, right: float,
           n_points: int, eps: float) -> float: 
    # solver finds point between left and right that maximizes f
    while abs(right - left) > eps:
        points = linspace(left, right, n_points)
        values = get_function_values(f, points)
        i_max = get_index_max_value(values)
        x_max = points[i_max]
        left, right = get_new_left_right_points(i_max, points)
    return (left + right) / 2


left = da_initial_offset
da_optimal = solver(calc_pipe, 
                    left=da_initial_offset, 
                    right=3-da_initial_offset,
					n_points=n_points,
                    eps=eps)

