#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Heuristica (object):
    """ Classe base de heurísticas. """

    def __init__ (self, n):
        self.n = n

    def _lde(self, x):
        """ Linha que X deveria estar """
        return x==0 and self.n-1 or (x-1)/self.n

    def _cde(self, x):
        """ Coluna que X deveria estar """
        return x==0 and self.n-1 or (x-1)%self.n


    def _peso(self, x, i, j):
        if x ==0: return 0
        else: return abs(self._lde(x) - i) + abs(self._cde(x) - j)

    def calcula (self, *args, **kwds):
        raise Exception("OPS!")

    def terminou(self,nodo):
        return nodo.peso - nodo.altura


class cebola(Heuristica):
    """ Calcula o peso de um tabuleiro, ou a alteracao de peso em um
    tabuleiro após uma jogada.
    n -> tamanho do tabuleiro (assume-se que seja quadrático) """
    __name__ = 'cebola'
    def __init__(self, n):
        Heuristica.__init__(self, n)
        self.matriz_multi = self._gera_matriz_multi()

    def calcula(self, tab, peso_pai=None, jogada=None):
        """ Calcula peso do tabuleiro inteiro ou a diferença dele
            para uma jogada.
            Recebe um tabuleiro. O peso do pai do tabuleiro deve ser
            passado caso uma jogada seja passada também. """

        if jogada != None:
            tava = jogada['ondetava']
            foi = jogada['ondefoi']
            valor = tab[foi[0]][foi[1]]
            peso_velho = self._peso(valor,tava[0],tava[1])
            peso_novo = self._peso(valor,foi[0],foi[1])
            mult = self.matriz_multi[self._lde(valor)][self._cde(valor)]
            return (peso_novo - peso_velho)*mult

        peso = 0
        for i in range(tab.n):
            for j in range(tab.n):
                valor = tab[i][j]
                dif_pos = self._peso(valor, i, j)
                mult = self.matriz_multi[self._lde(valor)][self._cde(valor)]
                peso += dif_pos*mult

        return peso

    def _gera_matriz_multi(self):
        n = self.n
        tab_multi = [[None]*n for i in range(n)]

        # FUNCIONA
        cont = n-1
        for i in range(n):
            for j in range(i,cont+i+1):
                tab_multi[i][j] = cont
                tab_multi[j][i] = cont
            cont -= 1

        return tab_multi

class cebola_com_somadora(cebola):

    def __init__(self,n):
        cebola.__init__(self,n)
        self.max_heuristica = self._max_heuri()

    def _max_heuri(self):
        count = 0
        for i in self.matriz_multi:
            for j in i:
                count += j
        return count

    def calcula(self, tab, peso_pai=None, jogada=None):
        """ Calcula peso do tabuleiro inteiro ou a diferença dele
            para uma jogada.
            Recebe um tabuleiro. O peso do pai do tabuleiro deve ser
            passado caso uma jogada seja passada também. """

        if jogada != None:
            tava = jogada['ondetava']
            foi = jogada['ondefoi']
            valor = tab[foi[0]][foi[1]]
            valort = tab[tava[0]][tava[1]]

            mult = self.matriz_multi[self._lde(valor)][self._cde(valor)]
            multtava = self.matriz_multi[self._lde(valort)][self._cde(valort)]

            peso_velho = self._peso(valor,tava[0],tava[1])+multtava
            peso_novo = self._peso(valor,foi[0],foi[1])+mult
            print 'deltanovo,deltavelho,multi,resultado'
            print peso_novo,peso_velho,mult,peso_novo-peso_velho
            return peso_novo - peso_velho

        peso = 0
        for i in range(tab.n):
            for j in range(tab.n):
                valor = tab[i][j]
                dif_pos = self._peso(valor, i, j)
                mult = self.matriz_multi[self._lde(valor)][self._cde(valor)]
                peso += dif_pos+mult

        print 'peso(tab inicial): ',peso
        return peso

    def terminou(self,nodo):
        return nodo.peso - nodo.altura - self.max_heuristica

class layers (cebola):
    """ Heuristica que prioriza as primeiras linhas. """
    def _gera_matriz_multi(self):
        """ Funciona como a heuristica cebola.  Mas a matriz
        multiplicadora é formada sendo que a linha i tem valor igual a
        n-i.  A posição do espaço vazio (elemento 0) tem valor igual
        azero (0)"""

        n = self.n

        tab_multi = [[i]*n for i in range(n,0,-1)]
        tab_multi[-1][-1] = 0

        return tab_multi

class manhattan(Heuristica):
    __name__ = "manhattan"
    """ Calcula o peso de um tabuleiro, ou a alteracao de peso em um
    tabuleiro após uma jogada.
    n -> tamanho do tabuleiro (assume-se que seja quadrático) """
    def __init__(self, n):
        Heuristica.__init__(self,n)

    def calcula(self, tab, peso_pai=None, jogada=None):
        """ Calcula peso do tabuleiro inteiro ou a diferença dele
            para uma jogada.
            Recebe um tabuleiro. O peso do pai do tabuleiro deve ser
            passado caso uma jogada seja passada também. """

        if jogada != None:
            tava = jogada['ondetava']
            foi = jogada['ondefoi']
            valor = tab[foi[0]][foi[1]]
            peso_velho = self._peso(valor,tava[0],tava[1])
            peso_novo = self._peso(valor,foi[0],foi[1])
            return (peso_novo - peso_velho)

        peso = 0
        for i in range(tab.n):
            for j in range(tab.n):
                valor = tab[i][j]
                dif_pos = self._peso(valor, i, j)
                peso += dif_pos

        return peso
