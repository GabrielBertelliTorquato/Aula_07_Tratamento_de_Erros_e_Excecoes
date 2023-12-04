# 2. Escreva um programa que solicita ao usuário uma data no formato "dd/mm/aaaa"
# e verifica se ela é válida. Use um bloco `try/except` para tratar o caso em que o
# usuário digita uma data inválida e lance uma exceção personalizada com a
# mensagem “Data inválida”.

def verifica_data(data_str):
    try:
        dia, mes, ano = map(int, data_str.split('/'))
        if 1 <= dia <= 31 and 1 <= mes <= 12 and 1900 <= ano <= 2100:
            return True
        else:
            raise Exception("Data inválida")
    except ValueError or Exception:
        raise Exception("Data inválida")


try:
    data = input("Digite uma data (dd/mm/aaaa): ")
    if verifica_data(data):
        print("Data válida!")
except Exception as e:
    print(f"Erro: {e}")
