# 17. Escreva um programa que contenha um loop infinito e trate exceções para permitir
# ao usuário interrompê-lo.

while True:
    try:
        resposta = input("Digite 's' para sair: ")
        if resposta.lower() == 's':
            break
    except KeyboardInterrupt:
        print("Loop interrompido pelo usuário.")
        break
    except Exception as e:
        print(f"Erro: {e}")
