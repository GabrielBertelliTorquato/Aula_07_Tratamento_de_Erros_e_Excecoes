# 8. Escreva uma função que recebe uma lista de strings como argumento e retorna
# uma nova lista com estas strings ordenadas alfabeticamente. Use um bloco
# `try/except` para tratar o caso em que a lista contém algum elemento que não é
# uma string e lance uma exceção personalizada com a mensagem “Lista inválida”.

def ordenar_lista(lista):
    try:
        if not all(isinstance(item, str) for item in lista):
            raise Exception("Lista inválida")
        return sorted(lista)
    except Exception as e:
        raise Exception(f"Erro: {e}")


try:
    lista_strings = input("Digite uma lista de strings separadas por espaço: ").split()
    resultado = ordenar_lista(lista_strings)
    print(f'Lista ordenada: {resultado}')
except Exception as e:
    print(f"Erro: {e}")
