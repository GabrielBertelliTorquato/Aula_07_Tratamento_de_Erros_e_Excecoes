# 11. Crie um programa que leia as configurações de um arquivo e trate exceções caso o
# arquivo contenha erros de formatação.

def ler_configuracoes(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            pass

    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
    except IOError:
        print("Erro: Problema ao ler o arquivo.")
    except Exception as e:
        print(f"Erro de formatação no arquivo: {e}")
