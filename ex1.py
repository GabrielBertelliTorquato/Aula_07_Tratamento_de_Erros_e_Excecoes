# 1. Escreva uma função que recebe dois números como argumentos e retorna a
# divisão do primeiro pelo segundo. Use um bloco try/except para tratar o caso em
# # que o segundo número é zero e lance uma exceção personalizada com a
# # mensagem "Divisão por zero não permitida".

def divisao(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        raise Exception("Divisão por zero não permitida")


try:
    resultado = divisao(10, 0)
    print(resultado)
except Exception as e:
    print(f"Erro: {e}")
