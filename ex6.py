# 6. Escreva uma função que recebe um número inteiro positivo como argumento e
# retorna o fatorial desse número. Use um bloco `try/except` para tratar o caso em
# que o argumento é negativo ou não é um inteiro e lance uma exceção
# personalizada com a mensagem “Argumento inválido”.

def fatorial(n):
    try:
        if n < 0 or not isinstance(n, int):
            raise Exception("Argumento inválido")
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado
    except Exception as e:
        raise Exception(f"Erro: {e}")


try:
    numero = int(input("Digite um número inteiro positivo: "))
    print(f'O fatorial de {numero} é {fatorial(numero)}')
except Exception as e:
    print(f"Erro: {e}")
