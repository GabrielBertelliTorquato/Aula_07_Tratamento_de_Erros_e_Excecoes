# 15. Escreva um programa que divida uma lista em partes iguais e trate exceções se o
# número de partes não for válido.

def dividir_lista(lista, num_partes):
    try:
        if len(lista) % num_partes != 0:
            raise ValueError("Número inválido de partes")
        
        tamanho_parte = len(lista) // num_partes
        partes = [lista[i:i + tamanho_parte] for i in range(0, len(lista), tamanho_parte)]
        return partes
    except ValueError as e:
        print(f"Erro: {e}")

try:
    minha_lista = [1, 2, 3, 4, 5, 6, 7, 8]
    num_partes = int(input("Digite o número de partes desejadas: "))
    resultado = dividir_lista(minha_lista, num_partes)
    print(f"Lista dividida: {resultado}")
except Exception as e:
    print(f"Erro: {e}")