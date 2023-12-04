# 18. Crie um programa que trate exceções aninhadas em um bloco `try/except`.

try:
    try:
        resultado = 10 / 0
    except ZeroDivisionError:
        raise ValueError("Erro de divisão por zero.")
except ValueError as e:
    print(f"Erro: {e}")
except Exception as e:
    print(f"Erro externo: {e}")