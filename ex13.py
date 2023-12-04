# 13. Escreva um programa que trate uma exceção genérica, como `Exception`, e
# imprima uma mensagem personalizada.

try:
    resultado = 10 / 0
except Exception as e:
    print(f"Erro: {e}")
 