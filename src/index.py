from compile import compile_afd

if __name__ == '__main__':    
    a = compile_afd()
    resultado = a.get_categorias("\"ab\"nN\"aabbc dbbd\" n n NN")
    print(a)
    print(resultado)    
    # assert ['q3', 'q1', 'q1', 'q3', 'q1', 'q1', 'q1', 'q1'] == resultado