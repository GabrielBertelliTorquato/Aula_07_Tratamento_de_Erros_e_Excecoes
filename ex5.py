# 5. Escreva um código que tente abrir um arquivo com o modo de escrita, porém o
# arquivo já existe. Se ocorrer uma exceção, imprima uma mensagem de erro.

try:
    with open("arquivo_existente.txt", 'x') as arquivo:
        arquivo.write("Olá, mundo!")
except FileExistsError:
    print("Erro: O arquivo já existe.")
