# 12. Peça ao usuário para digitar uma chave e, em seguida, tente acessar um valor em
# um dicionário. Trate exceções caso a chave não exista.

meu_dicionario = {"chave1": "valor1", "chave2": "valor2"}

try:
    chave = input("Digite uma chave: ")
    valor = meu_dicionario[chave]
    print(f"Valor encontrado: {valor}")
except KeyError:
    print("Erro: Chave não encontrada no dicionário.")
except Exception as e:
    print(f"Erro: {e}")