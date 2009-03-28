class heuristica(object):
    def __init__(self, tab):
        self.tab = tab
        self.matriz_multi = self._gera_matriz_multi()

    def _h(self,x):
        n = self.tab.n
        if x <= n:
            return n-1
        elif x % n == 0:
            return n-x/n
        else:
            return n-x%n

    def _gera_matriz_multi(self):
        n = self.tab.n
        tab_multi = [[None]*n for i in range(n)]
        cont = n-1
        for i in range(n):
            for j in range(i,cont+i+1):
                tab_multi[i][j] = cont
                tab_multi[j][i] = cont
            cont -= 1

        return tab_multi
