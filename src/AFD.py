from Estado import Estado

class AFD:
    def __has_estados_duplicados(self, estados) -> bool:
        visitados = set()
        duplicados = [i for i in estados if len([j for j in visitados if j.id == i.id]) != 0 or (visitados.add(i) or False)]
        return len(duplicados) != 0
        
    def __init__(self, inicial: Estado, estados: list[Estado], finais: list[Estado]):
        if len(estados) < len(finais):
            raise Exception("O conjunto de estados é menor que o de estados finais.")
        
        if len(estados) == 0 or len(finais) == 0:
            raise Exception("O AFD deve possuir ao menos 1 estado.")

        if inicial not in estados:
            raise Exception("O estado inicial também deve estar na lista de estados.")

        if self.__has_estados_duplicados(estados):
            raise Exception("Há estados duplicados.")

        if self.__has_estados_duplicados(finais):
            raise Exception("Há estados finais duplicados.")

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
            if e.id == estado.id:
                return True
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
                if self.is_estado_final(estado_anterior) and cadeia_entrada[i] == " ":
                    categorias.append(estado_anterior.id)
                elif cadeia_entrada[i] != " ":
                    categorias.append("NIN")
        
        if self.is_estado_final(estado):
            categorias.append(estado.id)
        else:
            categorias.append("NIN")
        
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