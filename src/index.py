from Estado import Estado
from Transicao import Transicao
from ADF import AFD

if __name__ == '__main__':

    q0 = Estado("q0")
    q1 = Estado("q1")
    q2 = Estado("q2")
    q3 = Estado("q3")

    q0_q1 = Transicao(q0, ["n", "N"], q1)
    q0_q2 = Transicao(q0, ["\""], q2)
    q2_q3 = Transicao(q2, ["\""], q3)
    q2_q2 = Transicao(q2, ["a", "b", "c", "d", " "], q2)
    
    a = AFD(
        inicial=q0, 
        estados=[q0, q1, q2, q3],
        finais=[q1, q3]
    )

    resultado = a.get_categorias("\"ab\"nN\"aabbc dbbd\" n n NN")
    
    print(a)
    print(resultado)
    
    assert ['q3', 'q1', 'q1', 'q3', 'q1', 'q1', 'q1', 'q1'] == resultado