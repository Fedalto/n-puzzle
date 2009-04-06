#!/usr/bin/env python

from solver import Solver
from tabuleiro import Tabuleiro,random_tab
import cProfile

tam_tabuleiro = 3
#tab_teste = [[5, 0, 2, 8],[13, 11, 1, 6],
#                  [7, 15, 12, 14],[3, 9, 4, 10]]

"""tab_teste = [[1, 2, 3, 4, 5, 6, 7, 8],
             [9, 10, 11, 12, 13, 14, 15, 16],
             [17, 18, 19, 20, 21, 22, 23, 24],
             [25, 26, 27, 28, 29, 30, 31, 32],
             [33, 34, 35, 36, 37, 46, 38, 40],
             [41, 50, 42, 44, 0, 45, 39, 47],
             [49, 59, 60, 51, 53, 54,63, 48],
             [57, 58, 52, 43, 61, 62, 56, 55]]
"""
tab_teste = random_tab(tam_tabuleiro,tam_tabuleiro**10).get_tab()

s = Solver(n=tam_tabuleiro,tabini=tab_teste)

cProfile.run('s.magic()')
