#!/bin/env python


# Python library
import random
import copy

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
        self.zero_pos = self.find(0)

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
#         print a, b, x, y
        if a+x < 0 or b+y < 0 or a+x > self.n-1 or b+y > self.n-1:
#            print a, b, x, y
            return None
        self.__tab[a][b] = self.__tab[a+x][b+y]
        self.__tab[a + x][b + y] = 0
        self.zero_pos = (a + x, b + y)
        return True #?
    
    def get_tab(self):
        return self.__tab

    def copy (self):
        return copy.deepcopy(self)

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
