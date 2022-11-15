from Estado import Estado

class AFD:
    def __init__(self, inicial: Estado, estados: list[Estado], finais: list[Estado]):
        self.inicial = inicial
        self.estados = estados
        self.finais = finais

    def get_next_estado(self, current_estado, simbolo_entrada):
        for transicao in current_estado.transicoes:
            if simbolo_entrada in transicao.simbolos:
                return transicao.estado_destino
        return None

    def is_estado_final(self, estado: Estado):
        for e in self.finais:
            if e.id == estado.id and len(e.transicoes) == len(estado.transicoes):
                ok = True
                if len(e.transicoes) == 0:
                    return ok
                for i in range(len(e.transicoes)):
                    ok = ok and (e.transicoes[i] == estado.transicoes[i])
                return ok
        return False

    def get_categorias(self, cadeia_entrada):
        estado: Estado = self.inicial
        categorias: list[str] = []

        for i in range(len(cadeia_entrada)):
            estado_anterior: Estado = estado
            estado = self.get_next_estado(estado, cadeia_entrada[i])
        
            if estado == None:
                estado = self.inicial
                print(f'Reiniciou; já processado: {cadeia_entrada[:i]}, restante: {cadeia_entrada[i:]}')
                if self.is_estado_final(estado_anterior):
                    categorias.append(estado_anterior.id)
            elif self.is_estado_final(estado):
                categorias.append(estado.id)
                estado = self.inicial
        
        return categorias

    def __str__(self):
        afd = "Estado inicial: %s\nEstados Finais: %s\n" % (self.inicial.id, [i.id for i in self.finais])
        for estado in self.estados:
            afd += estado
        return afd

    def __add__(self, other):
        return str(self) + other

    def __radd__(self, other):
        return other + str(self)