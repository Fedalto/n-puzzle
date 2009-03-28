class heuristica(object):
    def __init__(self, tab):
        self.tab = tab
        self.matriz_multi = self._gera_matriz_multi()


    def _lde(self, x):
        """ Linha que X deveria estar """
        return x-1%self.tab.n

    def _cde(self, x):
        """ Coluna que X deveria estar """
        return x-1/self.tab.n

    def _peso(self, x, i, j):
        return abs(self._lde(x) - 1) + abs(self._cde(x) - j)

    def calcula(self, no_pai, jogada=None):
        """ Calcula peso do tabuleiro inteiro ou a diferença dele
            para uma jogada """
        tab = no_pai.tab

        if jogada != None:
            tava = jogada.ondetava
            foi = jogada.ondefoi
            valor = tab[foi[0],foi[1]]
            peso_velho = self._peso(valor,tava[0],tava[1])
            peso_novo = self._peso(valor,foi[0],foi[1])
            return no_pai.peso - peso_velho-peso_novo

        peso = 0
        for i in range(tab.n):
            for j in range(tab.n):
                valor = tab[i][j]
                dif_pos = self._peso(valor, i, j)
                peso += dif_pos * self.matriz_multi[i][j]

        return peso

    def _h(self,x):
        n = self.tab.n
        if x <= n: return n-1
        else: return (n-1)-((x-1)%n)

    def _gera_matriz_multi(self):
        n = self.tab.n
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
