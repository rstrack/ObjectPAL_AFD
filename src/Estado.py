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