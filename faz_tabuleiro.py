#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Python library
import random
import copy

movimento = {'right' : (0,-1),
             'left' : (0,1),
             'up' : (1,0),
             'down' : (-1,0)}

class Tabuleiro (object):
    ''' Classe que representa o tabuleiro.
    E' implementado como uma lista de listas.
    O elemento com valor igual a 0 (zero)
    representa o espaco em vazio.'''

    def __init__ (self, lista,zero_pos=None):
        ''' Recebe uma lista de listas e
        retorna um objeto Tabuleiro. '''
        self.n = len(lista)
        self.size = self.n**2
        self.__tab = lista
        if not zero_pos:
            self.zero_pos = self.find(0)
        else:
            self.zero_pos = zero_pos

    def __str__ (self):
        s = ''
        print self.n
        for i in range(self.n):
            for j in range(self.n):
                digit = self[i][j]
                s += '%2d ' % self[i][j]
            s += '\n'
        return s

    def __getitem__ (self, item):
        return self.__tab.__getitem__(item)

    def find (self, num):
        for line in self.__tab:
            if num in line:
                break

        # Retorna (linha,coluna) do elemento 0
        return (self.__tab.index(line), line.index(num))

    def swap_test(self, (x,y)):
        a, b = self.zero_pos
        if a+x < 0 or b+y < 0 or a+x > self.n-1 or b+y > self.n-1:
            return False
        else:
            return True

    def swap (self, (x, y) ):
        a, b = self.zero_pos
        self.__tab[a][b] = self.__tab[a+x][b+y]
        self.__tab[a + x][b + y] = 0
        self.zero_pos = (a + x, b + y)

    def get_tab(self):
        return self.__tab

    def copy (self):
        #return copy.deepcopy(self)
        #return Tabuleiro(copy.deepcopy(self.get_tab()))
        return Tabuleiro([copy.copy(i) for i in self.get_tab()],self.zero_pos)
        #return Tabuleiro([i[:] for i in self.get_tab()],self.zero_pos)

def random_tab (n=4, n_of_mov=10):
    ''' Cria um tabuleiro resolvível aleatorio de NxN elementos e
        no máximo n_of_mov movimentos '''
    size = n**2
    l = [i for i in range(1,size)]
    l.append(0)
    tab_hash = {}

    tab = []
    for i in range(0,size, n):
        tab.append(l[i:i+n])


    tab = Tabuleiro(tab)
    tab_final = tab
    for i in range(n_of_mov):
        while True:
            mov = random.choice(movimento.values())
            if tab.swap_test(mov):
                tab.swap(mov)
                tmptab = hash(str(tab.get_tab()))
                if not tab_hash.has_key(tmptab):
                    tab_final = tab
                    tab_hash[tmptab] = None
                    break

    return tab_final

def cria_arquivo(prefix="",suffix="",ext=".txt"):
    prefix=str(prefix)+'x'+str(prefix)+'-'
    suffix=str(suffix).replace('**','up')
    prefix=prefix+suffix+'_'
    return open(mktemp(prefix=prefix,suffix=ext,dir='.'),'w')

if __name__ == "__main__":
    import sys
    from tempfile import mktemp
    tam = sys.argv[1]
    if tam == '-h' or tam == "--help":
        print "%s <N> <numero_de_movimentos>"%sys.argv[0]
        print "\t N -> tamanho do tabuleiro (serah NxN)"
        print "\t numero_de_movimentos -> numero de vezes que o NULL ira"
        print "\t\tmudar de lugar. O que >NAO< corresponde ao numero de"
        print "\t\tmovimentos necessarios para terminar o jogo."
        print "\t\tUSE POTENCIA. Ex: 2**10, 5**8"
        print "\n\tAo final da execucao o programa cria um arquivo que"
        print "\teh a concatenacao de N com numero_de_movimentos mais"
        print "\talguns caracteres aleatorios."
        sys.exit(0)

    n_of_mov = sys.argv[2]

    tabuleiro = random_tab(int(tam),eval(n_of_mov)).get_tab()

    arquivo = cria_arquivo(tam,n_of_mov)
    arquivo.write(str(tam)+'\n')
    for linha in tabuleiro:
        for elemento in linha:
            arquivo.write(str(elemento)+" ")
        arquivo.write('\n')
    print "Arquivo gerado: ",arquivo.name

