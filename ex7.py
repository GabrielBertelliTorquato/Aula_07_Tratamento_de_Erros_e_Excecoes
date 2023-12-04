# 7. Escreva uma função que recebe uma string como argumento e retorna o número
# de vogais contidas nessa string. Use um bloco `try/except` para tratar o caso em
# que o argumento não é uma string e lance uma exceção personalizada com a
# mensagem “Argumento inválido”.

def contar_vogais(texto):
    try:
        if not isinstance(texto, str):
            raise Exception("Argumento inválido")
        vogais = "aeiouAEIOU"
        qtd_vogais = sum(1 for char in texto if char in vogais)
        return qtd_vogais
    except Exception as e:
        raise Exception(f"Erro: {e}")


try:
    texto = input("Digite uma string: ")
    print(f'Número de vogais: {contar_vogais(texto)}')
except Exception as e:
    print(f"Erro: {e}")
