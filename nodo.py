# Proposta de representacao da jogada.
# E' um dict de tuplas (linha,coluna) que indicam 
# onde o espaco vazio deve ir.
# O nome do movimento e' referente ao quadrado
# que se movimenta sobre o espaco vazio.
movimento = {'right' : (0,-1),
             'left' : (0,1),
             'up' : (1,0),
             'down' : (-1,0)}


class Nodo(object):
    def __init__(self, tab, pai, peso, jogada, altura):
        self.tab = tab
        self.pai = pai
        self.peso = peso
        self.altura = altura
        self.jogada = jogada

