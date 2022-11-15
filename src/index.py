from compile import compile_afd
from categorias import get_categorias

if __name__ == '__main__':    
    categorias = get_categorias()
    
    a = compile_afd()
    print(a)
    
    resultado = a.get_categorias("\"ab\"nN\"aabbc dbbd\" n n NN")
    print(resultado)

    print([categorias[x] for x in resultado])
    
    assert ['q3', 'q1', 'q1', 'q3', 'q1', 'q1', 'q1', 'q1'] == resultado