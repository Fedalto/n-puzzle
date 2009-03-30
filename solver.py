import tabuleiro
from heuristica import heuristica
from nodo import nodo

class Solver (object):
    def __init__(self, n=3, tabini=None):
        self.heuristica = heuristica()
        self.lista_nodos = []
        self.n = n
        self.num_de_jogadas = 1

        # Se usuário não forçou um tabuleiro inicial, cria um aleatório
        if not tabini:
            tabini = tabuleiro.random_tab(self.n)

        tabini = tabuleiro.Tabuleiro(tabini)

        # Calcula peso do primeiro tabuleiro
        peso = self.heuristica.calcula(tabini.tab)

        # Cria um nodo
        nodoini = nodo(tabini,None,peso,None,1)

        # Adiciona nodo a lista de nodos
        self.adiciona_nodo(nodoini)

    def adiciona_nodo(self, nodo):
        """ Cada item da lista possui [peso,nodo] """

        self.lista_nodos.append([nodo.peso,nodo])
        self.ordena_lista_nodos()

    def ordena_lista(self):
        self.lista_nodos.sort(cmp=lambda x,y: x[0] - y[0])

    def prox_nodo (self):
        pass

    def gera_filhos (self, nodo):
        # -> faz copias dos nodos
        # -> aplica os movimentos as nodos (right, left,
        #    up, down)
        # -> Recalcula o peso do nodo.
        # -> Insere filhos na lista
        pass
