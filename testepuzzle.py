#!/usr/bin/env python

from solver import Solver
from heuristica import *
from tabuleiro import Tabuleiro,random_tab
import cProfile, resource, sys, time

def le_arquivo(arquivo):
    linhas = open(arquivo,'r').readlines()[1:]
    size = len(linhas)
    tab = ([l.split() for l in linhas])
    for linha in range(size):
        for coluna in range(size):
            tab[linha][coluna] = int(tab[linha][coluna])
    return tab

def cpu_time():
    return resource.getrusage(resource.RUSAGE_SELF)[0]
    #return time.time()

def usage():
    print "Uso: heuristica (-f arquivo|-r tamanho movimentos)"

def solver(heuri,tab):
    tam_tabuleiro = len(tab[0])
    print 'Tabuleiro inicial'
    print Tabuleiro(tab)
    c1 = cpu_time()
    s = Solver(n=tam_tabuleiro,tabini=tab,heuristica=eval(heuri))
    n_mov,sol = s.magic()
    cf = cpu_time() - c1
    print "Num. de movimentos, tempo"
    print n_mov,cf

if __name__ == "__main__":
    heuri = sys.argv[1]
    argtab = sys.argv[2]
    if argtab == '-h':
        usage()
    if argtab == "-f":
        tab = le_arquivo(sys.argv[3])
        solver(heuri,tab)
    elif argtab == "-r":
        tab = random_tab(int(sys.argv[3]),int(sys.argv[4])).get_tab()
        solver(heuri,tab)

