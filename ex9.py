# 9. Escreva um programa que solicite ao usuário um índice e, em seguida, tente
# acessar um elemento em uma lista. Trate exceções caso o índice esteja fora dos
# limites da lista.

lista = [1, 2, 3, 4, 5]

try:
    indice = int(input("Digite um índice: "))
    elemento = lista[indice]
    print(f"Elemento encontrado: {elemento}")
except IndexError:
    print("Erro: Índice fora dos limites da lista.")
except ValueError:
    print("Erro: Índice deve ser um número inteiro.")

