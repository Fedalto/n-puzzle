#!/bin/env python


# Python library
import random

class Tabuleiro (object):
    ''' Classe que representa o tabuleiro.
    E' implementado como uma lista de listas. 
    O elemento com valor igual a 0 (zero)
    representa o espaco em vazio.'''

    def __init__ (self, n = 4):
        ''' Cria um tabuleiro aleatorio de NxN '''
        self.n = n
        self.size = self.n**2

        l = [i for i in range(self.size)]
        random.shuffle(l)

        self.__tab = []
        for i in range(0,self.size, n):
            self.__tab.append( l[i:i+n] )

    def __str__ (self):
        s = ''
        for line in self.__tab:
            s += str(line) + '\n'
        return s.rstrip()

    def __getitem__ (self, item):
        return self.__tab.__getitem__(item)



def main ():
    t = Tabuleiro(4)
    print t

if __name__ == '__main__':
    main()
