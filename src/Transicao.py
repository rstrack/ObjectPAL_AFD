import time
from Estado import Estado

class Transicao:
    def __init__(self, estado_origem: Estado, simbolos: list[str], estado_destino: Estado, add_transicao: bool =  True):
        if (len(simbolos) == 0):
            raise Exception("É necessário ao menos um símbolo para criar a transição")

        self.estado_origem = estado_origem
        self.simbolos = simbolos
        self.estado_destino = estado_destino
        if add_transicao:
            self.estado_origem.add_transicao(self)

    def transicao_complexa(self) -> list[Estado]:
        _estados = []
        for simbolo in self.simbolos:
            est_i = self.estado_origem
            for i in range(len(simbolo)):
                if i == len(simbolo)-1:
                    t  = Transicao(est_i, simbolo[i], self.estado_destino)
                    est_i.add_transicao(t)
                    return
                est_f = Estado(f"q_aux_{int(time.time())}")
                _estados.append(est_f)
                t = Transicao(est_i, simbolo[i], est_f)
                est_i.add_transicao(t)
                est_i = est_f
        return _estados
            
    def __str__(self):
        return "(%s -- %s --> %s)" % (
            self.estado_origem.id, 
            self.simbolos, 
            self.estado_destino.id
        )

    def __add__(self, other):
        return str(self) + other

    def __radd__(self, other):
        return other + str(self)

    def equals(self, transicao):
        return (
            (self.estado_origem == transicao.estado_origem) 
            and (self.estado_destino == transicao.estado_destino)
            and (set(self.estados) == set(transicao.simbolos))
        )