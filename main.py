class Estado:
    def __init__(self, id):
        self.id = id
        self.transicoes = []
        
    def add_transicao(self, transicao):
        self.transicoes.append(transicao)

    def __str__(self):
        estado = "(%s):\n" % self.id
        for transicao in self.transicoes:
            estado += "\t" + transicao + "\n"
        return estado

    def __add__(self, other):
        return str(self) + other

    def __radd__(self, other):
        return other + str(self)

    def equals(self, estado):
        ok = (self.id == estado.id)
        if len(self.transicoes) == len(estado.transicoes):
            for i in range(len(self.transicoes)):
                ok = ok and (self.transicoes[i] == estado.transicoes[i])
            return ok
        else:
            return False

class Transicao:
    def __init__(self, estado_origem, simbolo, estado_destino):
        self.estado_origem = estado_origem
        self.simbolo = simbolo
        self.estado_destino = estado_destino

    def __str__(self):
        return "(%s -- %s --> %s)" % (self.estado_origem.id, self.simbolo, self.estado_destino.id)

    def __add__(self, other):
        return str(self) + other

    def __radd__(self, other):
        return other + str(self)

    def equals(self, transicao):
        return (self.estado_origem == transicao.estado_origem) and (self.simbolo == transicao.simbolo) and (self.estado_destino == transicao.estado_destino)

class AFD:
    def __init__(self, inicial: Estado, estados: list[Estado], finais: list[Estado]):
        self.inicial = inicial
        self.estados = estados
        self.finais = finais

    def get_next_estado(self, current_estado, simbolo_entrada):
        for transicao in current_estado.transicoes:
            if transicao.simbolo == simbolo_entrada:
                return transicao.estado_destino
        return None

    def equals(self, estados: list[Estado], estado: Estado):
        for e in estados:
            ok = (e.id == estado.id)
            if len(e.transicoes) == len(estado.transicoes):
                for i in range(len(e.transicoes)):
                    ok = ok and (e.transicoes[i] == estado.transicoes[i])
                return ok
        return False

    def accepts(self, string):
        estado = self.inicial
        for character in string:
            estado = self.get_next_estado(estado, character)
        return self.equals(self.finais, estado)

    def __str__(self):
        afd = "Estado inicial: %s\nEstados Finais: %s\n" % (self.inicial.id, [i.id for i in self.finais])
        for estado in self.estados:
            afd += estado
        return afd

    def __add__(self, other):
        return str(self) + other

    def __radd__(self, other):
        return other + str(self)


if __name__ == '__main__':

    s0 = Estado("s0")
    s1 = Estado("s1")
    s2 = Estado("s2")

    s0_1_1 = Transicao(s0, "<", s1)
    s1_2_1 = Transicao(s1, ">", s2)
    s1_2_2 = Transicao(s1, "=", s2)

    s0.add_transicao(s0_1_1)
    s1.add_transicao(s1_2_1)
    s1.add_transicao(s1_2_2)

    a = AFD(s0, [s0, s1, s2], [s1, s2])

    print(a)
    print(a.accepts('<>')) #True
    print(a.accepts('<')) #True
    print(a.accepts('<=')) #True