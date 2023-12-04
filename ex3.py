# 3. Escreva uma função que recebe uma lista de números como argumento e retorna a
# soma dos elementos da lista. Use um bloco `try/except` para tratar o caso em que
# a lista contém algum elemento que não é um número e lance uma exceção
# personalizada com a mensagem “Lista inválida”.

def soma_lista(lista):
    try:
        soma = sum([float(num) for num in lista])
        return soma
    except ValueError:
        raise Exception("Lista inválida")


try:
    numeros = input("Digite uma lista de números separados por espaço: ").split()
    resultado = soma_lista(numeros)
    print(f"Soma dos elementos: {resultado}")
except Exception as e:
    print(f"Erro: {e}")
