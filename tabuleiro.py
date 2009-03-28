#!/bin/env python

# Python library
import numpy


class Tabuleiro (object):

    def __init__ (self, dimensao = 4):
        self.n = dimensao**2
        self.tab = numpy.random.permutation(self.n)
        self.tab = self.tab.reshape(dimensao,dimensao)

    def __str__ (self):
        return self.tab.__str__()



def main ():
    t = Tabuleiro(4)
    print t

if __name__ == '__main__':
    main()
