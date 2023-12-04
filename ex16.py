# 16. Escreva um programa que manipule múltiplas exceções em um bloco `try/except`.

try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro de divisão por zero.")
except ArithmeticError:
    print("Erro aritmético.")
except Exception as e:
    print(f"Erro: {e}")