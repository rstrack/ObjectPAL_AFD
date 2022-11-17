from compile import compile_afd
from categorias import get_categorias

if __name__ == '__main__':    
    categorias = get_categorias()
    
    a = compile_afd()
    print(a)
    
    resultado = a.get_categorias("Not 9 < 8")
    print(resultado)

    print([categorias[x] for x in resultado])
