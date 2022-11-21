import sys
from src.objectPAL_Lexer import ObjectPAL_Lexer

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("É preciso passar o nome do arquivo para leitura na linha de comando. EX: input.txt")
    else:
        file_name = sys.argv[1]
        try:
            with open (file_name, "r", encoding="utf-8") as file:
                linhas = file.readlines()

                print(f'\nABRINDO ARQUIVO: {file_name}')
                lexer = ObjectPAL_Lexer()
                for linha in linhas:
                    lexer.input(linha)
                    flag = True
                    while(flag):
                        tok = lexer.token()
                        if tok: 
                            print(tok)
                        else:
                            flag = False
        except IOError as err:
            if err.errno == 2:
                print("Erro: Arquivo não encontrado no diretório raiz.")
            else:
                print("Erro ao abrir o arquivo indicado")
