from typing import Callable, List
from config import Pair


def calc_out(x: float, y: float, dx: float, p: float) -> float:
    return y * dx / (x + dx) - p * dx


def calc_pipe(da: float, lps: List[Pair], p: float) -> float:
    """
    calculate da after a "circle" 
    """
    db = calc_out(lps[0].quote, lps[0].base, da, p)
    dc = calc_out(lps[1].quote, lps[1].base, db, p)
    dd = calc_out(lps[2].quote, lps[2].base, dc, p)
    de = calc_out(lps[3].quote, lps[3].base, dd, p)
    da1 = calc_out(lps[4].quote, lps[4].base, de, p)
    return da1


def linspace(left: float, right: float, n: int) -> List[float]:
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


def get_function_values(f: Callable, lps: List[Pair], points: List[float], p: float) -> List[float]:
    """
    x is da in this case
    """
    values = [None] * len(points)
    for i, x in enumerate(points):
        values[i] = f(x, lps, p) - x
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


def solver(f: Callable, lps: List[Pair], p: float, left: float, right: float,
           n_points: int, eps: float) -> float: 
    # solver finds point between left and right that maximizes f
    while abs(right - left) > eps:
        points = linspace(left, right, n_points)
        values = get_function_values(f, lps, points, p)
        i_max = get_index_max_value(values)
        x_max = points[i_max]
        left, right = get_new_left_right_points(i_max, points)
    return (left + right) / 2


