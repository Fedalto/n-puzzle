#!/usr/bin/env python

from solver import Solver
from tabuleiro import Tabuleiro,random_tab
import cProfile

tab_teste = [[1, 2, 7, 3],[5, 6, 4, 8],[9, 11, 0, 12],[13, 10, 14, 15]]
#tab_teste = random_tab(4,50).get_tab()

s = Solver(n=4,tabini=tab_teste)

cProfile.run('s.magic()')
