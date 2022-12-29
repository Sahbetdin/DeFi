from collections import namedtuple

Pair = namedtuple("Pair",["base","quote"])
#givens
lps = [
	Pair(166740188573, 3753139396),
	Pair(766050680304, 724520588560),
	Pair(1051487855, 10457920653),
	Pair(2846977754550, 1722571966294),
	Pair(4310194783973, 22496742244741)
	]

for pair in lps:
	assert isinstance(pair.base, (int,float)), "Error! Check base value for input."
	assert isinstance(pair.quote, (int,float)), "Error! Check quote value for input."
p = 0.3/100

#serving params:
da_initial_offset = 0.001
n_points = 30 # number of segments for solver
eps = 1.e-5 #threshold used for solver
