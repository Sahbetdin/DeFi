from collections import namedtuple

Pair = namedtuple("Pair",["base","quote"])
#givens
lps = [
	Pair(166,3), 
	Pair(766, 724), 
	Pair(1, 10), 
	Pair(2846, 1722), 
	Pair(4_360, 22_500)]

p = 0.3/100

#serving params:
da_initial_offset = 0.001
n_points = 30 # number of segments for solver
eps = 1.e-5 #threshold used for solver
