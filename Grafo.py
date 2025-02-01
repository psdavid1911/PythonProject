class Grafo:

    nos = dict()

    def add_kno(self, vlr):
        if vlr not in self.nos.keys(): self.nos[vlr] = set()

    def add_aresta(self, vlr1, vlr2, bi=False):
        if vlr1 not in self.nos.keys():self.add_kno(vlr1)
        self.nos.get(vlr1).add(vlr2)
        if bi:self.add_aresta(vlr2, vlr1)

    def prt_grf(self):
        for chave in self.nos.keys():
            print(chave + ':')
            for elemento in self.nos[chave]:print('\t' + elemento)

    def percorre(self, entrada, meta):
        if entrada == meta:
            return meta
        for no in self.nos[entrada]:
            self.percorre(no, meta)





# Testes -------------------------------------------------------
if __name__ == '__main__':
    g = Grafo()
    g.add_kno('1') # no soziho
    g.add_kno('1') # no soziho duplicado
    g.add_aresta('1', '2')
    g.add_aresta('3', '4')
    g.add_aresta('4', '5', True) # bidirecional
    g.add_aresta('1', '3') # acrescentando
    g.add_aresta('1', '3') # duplicado
    g.add_aresta('1', '4') # acrescenta bidirecional
    g.prt_grf()
