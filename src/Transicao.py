from Estado import Estado

class Transicao:
    def __init__(self, estado_origem: Estado, simbolos: list[str], estado_destino: Estado):
        if (len(simbolos) == 0):
            raise Exception("É necessário ao menos um símbolo para criar a transição")

        self.estado_origem = estado_origem
        self.simbolos = simbolos
        self.estado_destino = estado_destino

        self.estado_origem.add_transicao(self)

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