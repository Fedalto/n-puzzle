#!/usr/bin/env python

from solver import Solver
from tabuleiro import Tabuleiro,random_tab
import cProfile

tam_tabuleiro = 8
#tab_teste = [[5, 14, 10, 9], [6, 8, 15, 2], [11, 13, 4, 7], [0, 12, 1, 3]]
tab_teste = random_tab(tam_tabuleiro,100).get_tab()

s = Solver(n=tam_tabuleiro,tabini=tab_teste)

cProfile.run('s.magic()')
