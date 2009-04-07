#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tabuleiro, sys
from heuristica import cebola,manhattan
from nodo import Nodo, movimento

class Solver (object):
    def __init__(self, n=3, tabini=None,heuristica=cebola):
        self.heuristica = heuristica(n)
        self.lista_nodos = []
        self.n = n
        self.hash_pais = {}
        self.hash_tab = {}
        self.hash_nodos = {}

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

        #self.lista_nodos.append([nodo.peso,nodo])
        if self.hash_nodos.has_key(nodo.peso):
            self.hash_nodos[nodo.peso].append(nodo)
        else:
            self.hash_nodos[nodo.peso] = [nodo]

        if nodo.peso not in self.lista_nodos:
            self.lista_nodos.append(nodo.peso)
            self.ordena_lista_nodos()
            #self.insere_ordenado(nodo.peso)

        self.hash_pais[nodo.id] = nodo

    def insere_ordenado(self,peso):
        for i, v in enumerate(self.lista_nodos):
            if peso <= v:
                self.lista_nodos.insert(i,peso)
                break
        else:
            self.lista_nodos.append(peso)

    def ordena_lista_nodos(self):
        self.lista_nodos.sort()

    def _cmp_nodos(self,x,y):
        return x[0]-y[0]

    def prox_nodo (self):
        idx = self.lista_nodos[0]
        todosnodos = self.hash_nodos[idx]
        if len(todosnodos) == 1: del self.lista_nodos[0]
        return todosnodos.pop(0)

    def gera_filhos (self, nodo):
        # -> faz copias dos nodos
        # -> aplica os movimentos as nodos (right, left,
        #    up, down)
        # -> Recalcula o peso do nodo.
        # -> Insere filhos na lista

        for nome_mov, mov in movimento.items():
            if not nodo.tab.swap_test(mov):
                continue
            else:
                novo_tab = nodo.tab.copy()
                novo_tab.swap(mov)

            htab = hash(str(novo_tab.get_tab()))
            if htab in self.hash_tab:
                continue
            self.hash_tab[htab] = None

            # Jogada INVERTIDA
            # Tudo e' relativo ao observador
            jogada = {'ondetava': novo_tab.zero_pos,
                      'ondefoi' : nodo.tab.zero_pos }

            incaltura = 1
            #incaltura = nodo.tab.n/2

            delta = self.heuristica.calcula(novo_tab, nodo.peso, jogada)
            novo_nodo = Nodo(novo_tab, len(self.hash_pais) ,nodo.id,
                    (nodo.peso + delta)+incaltura, nome_mov,
                    nodo.altura+incaltura)

            print novo_nodo.peso, novo_nodo.altura
            print novo_nodo.tab

            self.adiciona_nodo(novo_nodo)

    def magic (self):
        """ You want some magic??? Resolve tudo... """
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
        print "Construindo solução..."

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
        print "Número de movimentos necessários =",len(solution)

