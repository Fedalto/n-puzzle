#!/bin/env python


# Python library
import random

class Tabuleiro (object):
    ''' Classe que representa o tabuleiro.
    E' implementado como uma lista de listas. 
    O elemento com valor igual a 0 (zero)
    representa o espaco em vazio.'''

    def __init__ (self, lista):
        ''' Recebe uma lista de listas e
        retorna um objeto Tabuleiro. '''
        self.n = len(lista)
        self.size = self.n**2
        self.__tab = lista

    def __str__ (self):
        s = ''
        for line in self.__tab:
            s += str(line) + '\n'
        return s.rstrip()

    def __getitem__ (self, item):
        return self.__tab.__getitem__(item)

    def copy (self):
        return Tabuleiro(self.__tab)

def random_tab (n = 4):
    ''' Cria um tabuleiro aleatorio de NxN '''
    size = n**2
    l = [i for i in range(size)]
    random.shuffle(l)

    tab = []
    for i in range(0,size, n):
        tab.append( l[i:i+n] )

    return Tabuleiro(tab)


def main ():
    t = random_tab()
    print t
    print t.copy()

if __name__ == '__main__':
    main()
