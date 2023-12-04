# 10. Peça ao usuário para digitar um número inteiro e, em seguida, tente converter
# esse número em uma string. Trate a exceção que pode ocorrer.

try:
    numero = int(input("Digite um número inteiro: "))
    texto = str(numero)
    print(f"Número convertido para string: {texto}")
except ValueError:
    print("Erro: Entrada inválida. Digite um número inteiro.")
