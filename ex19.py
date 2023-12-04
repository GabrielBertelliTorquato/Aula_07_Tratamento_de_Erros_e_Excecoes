# 19. Escreva um programa que utilize o bloco `else` para tratar exceções.

try:
    resultado = 10 / 2
except ZeroDivisionError:
    print("Erro: Divisão por zero.")
else:
    print(f"Resultado da divisão: {resultado}")
finally:
    print("Executando o bloco finally.")