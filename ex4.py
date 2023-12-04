# 4. Escreva um programa que solicita ao usuário um nome de arquivo e tenta abri-lo
# para leitura. Use um bloco `try/except` para tratar o caso em que o arquivo não
# existe ou não pode ser aberto e lance uma exceção personalizada com a
# mensagem “Arquivo inválido”.

def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    except FileNotFoundError:
        raise Exception("Arquivo não encontrado")
    except IOError:
        raise Exception("Erro ao abrir o arquivo")


try:
    nome_arquivo = input("Digite o nome do arquivo: ")
    ler_arquivo(nome_arquivo)
except Exception as e:
    print(f"Erro: {e}")
