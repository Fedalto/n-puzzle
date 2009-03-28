class nodo(object):
    def __init__(self,tab,id_pai,peso,jogada_anterior,altura):
        self.tab = tab
        self.id_pai = id_pai
        self.peso = peso
        self.altura = altura
        self.jogada_anterior = jogada_anterior

    def gera_filhos(self):
        pass

    def _calcula_peso(self, jogada):
        pass
