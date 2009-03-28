# Proposta de representacao da jogada.
# E' um dict de tuplas (linha,coluna) que indicam 
# onde o espaco vazio deve ir.
# O nome do movimento e' referente ao quadrado
# que se movimenta sobre o espaco vazio.
movimento = {'right' : (0,-1),
             'left' : (0,1),
             'up' : (1,0),
             'down' : (-1,0)}


class nodo(object):
    def __init__(self,tab,id_pai,peso,jogada_anterior,altura):
        self.tab = tab
#         self.id_pai = id_pai
        self.peso = peso
        self.altura = altura
        self.jogada_anterior = jogada_anterior

#     def gera_filhos(self):
#         pass

    def copy (self):
        pass

    def _calcula_peso(self, jogada):
        pass
