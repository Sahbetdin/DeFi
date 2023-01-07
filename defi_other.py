from math import sqrt
import matplotlib.pyplot as plt
import sys 

b1 = 166740188573
a1 = 3753139396

c2 = 766050680304
b2 = 724520588560

d3 = 1051487855
c3 = 10457920653

e4 = 2846977754550
d4 = 1722571966294

a5 = 4310194783973
e5 = 22496742244741

p = 0.3/100

#functions for checking
def calc_out(x: float, y: float, dx: float, p: float) -> float:
    return y * dx / (x + dx) - p * dx

def plot_pipe(left=20_000_000, right=60_000_000, fee=0):
	x, y = [], []
	for da in range(left, right, 5000):
		x.append(da)
		db = calc_out(a1, b1, da, fee)
		dc = calc_out(b2, c2, db, fee)
		dd = calc_out(c3, d3, dc, fee)
		de = calc_out(d4, e4, dd, fee)
		da_prime = calc_out(e5, a5, de, fee)
		y.append(da_prime - da)
	return x, y

# without costs
beta = b1 / b2
gamma = c2 / c3
delta = d3 / d4
epsilon = e4 / e5

t = a5 * beta * gamma * delta * epsilon
u = 1 + beta + beta * gamma + beta * gamma * delta + beta * gamma * delta * epsilon
#da calculated by formula
da_formula = (sqrt(t * a1) - a1) / u
print(f'WITHOUT costs: da={da_formula}')

#checking via plotting the graph of f = da_prime - da
left = 30_000_000
right = 60_000_000
x, y = plot_pipe(left, right, fee=0)
plt.plot(x, y, color='black', label ='NO fees')
plt.title("coins 'da' after one 'circle'")
plt.xlabel('da')
plt.ylabel('da_prime - da')
plt.axvline(da_formula, color='blue', label='NO fees: max da')
plt.legend()
plt.show()

# with costs 
alpha = b1 / a1 - p
beta = c2 / b2 - p
gamma = d3 / c3 - p
delta = e4 / d4 - p
epsilon = a5 / e5 - p
A = b1 / a1 ** 2
B = c2 / b2 ** 2
G = d3 / c3 ** 2
D = e4 / d4 ** 2
E = a5 / e5 ** 2
prod = alpha * beta * gamma * delta * epsilon

first = beta * gamma * delta * epsilon * A
second = alpha ** 2 * gamma * delta * epsilon * B
third = (alpha * beta) ** 2 * delta * epsilon * G
fourth = (alpha * beta * gamma) ** 2 * epsilon * D
fifth = (alpha * beta * gamma * delta) ** 2 * E
#da calculated via retaining 1st order in expansion of 1/(1+x) function
da_formula_with_costs = (prod - 1) / (first + second + third + fourth + fifth) / 2
xx, yy = plot_pipe(20_000_000, right, fee=p)
print(f'   WITH costs: da={da_formula_with_costs}')

plt.plot(xx, yy, color='magenta', label ='WITH fees')
plt.title("coins 'da' after one 'circle'")
plt.xlabel('da')
plt.ylabel('da_prime - da')
plt.axvline(da_formula_with_costs, color='blue', label='WITH fees: max da')
plt.legend()
plt.show()
