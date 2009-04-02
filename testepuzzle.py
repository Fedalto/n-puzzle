#!/usr/bin/env python

from solver import Solver
from tabuleiro import Tabuleiro

tab_teste = [[1,2,3],[0,4,6],[7,5,8]]

s = Solver(n=3,tabini=tab_teste)

s.magic()
