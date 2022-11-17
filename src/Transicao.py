import uuid
from Estado import Estado

class Transicao:
    def __init__(self, estado_origem: Estado, simbolos: list[str], estado_destino: Estado):
        if (len(simbolos) == 0):
            raise Exception("É necessário ao menos um símbolo para criar a transição")

        self.estado_origem = estado_origem
        self.estado_destino = estado_destino
        
        _intermediarios = []
        for simbolo in simbolos:
            if len(simbolo) > 1:
                _intermediarios.extend(self.transicao_complexa(simbolo))
                simbolos.remove(simbolo)

        self.simbolos = simbolos
        self.estado_origem.add_transicao(self)

        self.__intermediarios = _intermediarios

    def get_intermediarios(self) -> list[Estado]: 
        return self.__intermediarios

    def transicao_complexa(self, simbolo) -> list[Estado]:
        _estados = []
        est_i = self.estado_origem
        for i in range(len(simbolo)-1):
            est_f = Estado(f"q_aux_{i}_{uuid.uuid4()}")
            _estados.append(est_f)
            Transicao(est_i, simbolo[i], est_f)
            est_i = est_f
        Transicao(est_i, simbolo[len(simbolo)-1], self.estado_destino)
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