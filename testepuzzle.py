#!/usr/bin/env python

from solver import Solver
from tabuleiro import Tabuleiro,random_tab
import cProfile

tab_teste = [[6, 5, 2, 3],[0, 1, 8, 4],[9, 10, 7, 11],[13, 14, 15, 12]]
#tab_teste = random_tab(4,50).get_tab()

s = Solver(n=4,tabini=tab_teste)

cProfile.run('s.magic()')
