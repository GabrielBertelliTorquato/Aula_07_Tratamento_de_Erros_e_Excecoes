# 14. Crie um programa que peça ao usuário para digitar uma senha com pelo menos 8
# caracteres. Trate exceções caso a senha seja muito curta.

try:
    senha = input("Digite uma senha com pelo menos 8 caracteres: ")
    if len(senha) < 8:
        raise ValueError("Senha muito curta. Deve ter pelo menos 8 caracteres.")
    print("Senha aceita!")
except ValueError as e:
    print(f"Erro: {e}")