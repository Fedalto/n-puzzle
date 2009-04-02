#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tabuleiro
from heuristica import heuristica
from nodo import Nodo, movimento

class Solver (object):
    def __init__(self, n=3, tabini=None):
        self.heuristica = heuristica(n)
        self.lista_nodos = []
        self.n = n
        self.hash_pais = {}
        self.hash_tab = {}

        # Se usuário não forçou um tabuleiro inicial, cria um aleatório
        if not tabini:
            tabini = tabuleiro.random_tab(self.n)
        else:
            tabini = tabuleiro.Tabuleiro(tabini)

        # Calcula peso do primeiro tabuleiro
        peso = self.heuristica.calcula(tabini)

        # Adiciona o tabuleiro na lista de hashs
        self.hash_tab[hash(str(tabini.get_tab()))] = None

        # Cria um nodo
        nodoini = Nodo(tabini, 0, None,peso,None,0)
        self.hash_pais[0] = nodoini

        # Adiciona nodo a lista de nodos
        self.adiciona_nodo(nodoini)

    def adiciona_nodo(self, nodo):
        """ Cada item da lista possui [peso,nodo] """

        self.lista_nodos.append([nodo.peso,nodo])
        self.hash_pais[nodo.id] = nodo
        self.ordena_lista_nodos()

    def ordena_lista_nodos(self):
        self.lista_nodos.sort(cmp=lambda x,y: x[0] - y[0])

    def prox_nodo (self):
        return self.lista_nodos.pop(0)[1]

    def gera_filhos (self, nodo):
        for nome_mov, mov in movimento.items():
            novo_tab = nodo.tab.copy()
            if not novo_tab.swap(mov):
                continue

            if str(novo_tab.get_tab()) in self.hash_tab:
                continue
            self.hash_tab[hash(str(novo_tab.get_tab()))] = None

            # Jogada INVERTIDA
            # Tudo e' relativo ao observador
            jogada = {'ondetava': novo_tab.zero_pos,
                      'ondefoi' : nodo.tab.zero_pos }

            delta = self.heuristica.calcula(novo_tab, nodo.peso, jogada)
            novo_nodo = Nodo(novo_tab, len(self.hash_pais) ,nodo.id,
                             nodo.peso + delta +1, nome_mov, nodo.altura+1)

            self.adiciona_nodo(novo_nodo)

        # -> faz copias dos nodos
        # -> aplica os movimentos as nodos (right, left,
        #    up, down)
        # -> Recalcula o peso do nodo.
        # -> Insere filhos na lista

    def magic (self):
        nodo = self.prox_nodo()
        while nodo.peso - nodo.altura:
            self.gera_filhos(nodo)
            nodo = self.prox_nodo()
        self.print_solucao(nodo)


    def print_solucao (self, nodo):
        ###
        #
        # Aki faz tratamento de subida dos nodos, empilhamento dos movimentos
        # e impressao do resultado, alem do cafe.
        solution = []

        while nodo.id_pai:

            solution.append(nodo)
            nodo = self.hash_pais[nodo.id_pai]
        solution.append(nodo)

        solution.reverse()

        print '\nSOLUCAO\n'
        for step in solution:
            print step.tab
            print
