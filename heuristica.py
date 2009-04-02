#!/usr/bin/env python
# -*- coding: utf-8 -*-

class heuristica(object):
    """ Calcula o peso de um tabuleiro, ou a alteracao de peso em um
    tabuleiro após uma jogada.
    n -> tamanho do tabuleiro (assume-se que seja quadrático) """
    def __init__(self, n):
        self.n = n
        self.matriz_multi = self._gera_matriz_multi()

    def _lde(self, x):
        """ Linha que X deveria estar """
        return (x-1)/self.n

    def _cde(self, x):
        """ Coluna que X deveria estar """
        return (x-1)%self.n

    def _peso(self, x, i, j):
        return abs(self._lde(x) - i) + abs(self._cde(x) - j)

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

    def _h(self,x):
        n = self.n
        if x <= n: return n-1
        else: return (n-1)-((x-1)%n)

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

        # ULYSSES
        #cont = 1
        #for i in range(n):
        #    for j in range(n):
        #        tab_multi[i][j] = self._h(cont)
        #        cont +=1

        return tab_multi
