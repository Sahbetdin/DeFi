import logging as lgn
from utils import *
import config as cnf
import sys
lgn.basicConfig(format='%(message)s', level=lgn.NOTSET)


left = cnf.da_initial_offset
right = cnf.lps[0].quote - left

da_optimal = solver(f=calc_pipe,
                    lps=cnf.lps,
                    p=cnf.p,
                    left=left, 
                    right=right,
                    n_points=cnf.n_points,
                    eps=cnf.eps)

lgn.info(da_optimal)

