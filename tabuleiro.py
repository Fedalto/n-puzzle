#!/bin/env python
# -*- coding:utf-8 -*-

# Python library
import random
import copy
from nodo import movimento

class Tabuleiro (object):
    ''' Classe que representa o tabuleiro.
    E' implementado como uma lista de listas.
    O elemento com valor igual a 0 (zero)
    representa o espaco em vazio.'''

    def __init__ (self, lista,zero_pos=None):
        ''' Recebe uma lista de listas e
        retorna um objeto Tabuleiro. '''
        self.n = len(lista)
        self.size = self.n**2
        self.__tab = lista
        if not zero_pos:
            self.zero_pos = self.find(0)
        else:
            self.zero_pos = zero_pos

    def __str__ (self):
        s = ''
        for line in self.__tab:
            s += str(line) + '\n'
        return s.rstrip()

    def __getitem__ (self, item):
        return self.__tab.__getitem__(item)

    def find (self, num):
        for line in self.__tab:
            if num in line:
                break

        # Retorna (linha,coluna) do elemento 0
        return (self.__tab.index(line), line.index(num))

    def swap (self, (x, y) ):
        a, b = self.zero_pos
        if a+x < 0 or b+y < 0 or a+x > self.n-1 or b+y > self.n-1:
            return False
        self.__tab[a][b] = self.__tab[a+x][b+y]
        self.__tab[a + x][b + y] = 0
        self.zero_pos = (a + x, b + y)
        return True

    def get_tab(self):
        return self.__tab

    def copy (self):
        #return copy.deepcopy(self)
        #return Tabuleiro(copy.deepcopy(self.get_tab()))
        return Tabuleiro([i[:] for i in self.get_tab()],self.zero_pos)

def random_tab (n=4, n_of_mov=10):
    ''' Cria um tabuleiro resolvível aleatorio de NxN elementos e
        no máximo n_of_mov movimentos '''
    size = n**2
    l = [i for i in range(1,size)]
    l.append(0)

    tab = []
    for i in range(0,size, n):
        tab.append(l[i:i+n])

    tab = Tabuleiro(tab)
    for i in range(n_of_mov):
        tab.swap(random.choice(movimento.values()))

    return tab


def main ():
    t = random_tab()
    print t
    print t.copy()

if __name__ == '__main__':
    main()
