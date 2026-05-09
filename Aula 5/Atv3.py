def contar_linhas(nome_arquivo):
    x = open(nome_arquivo, 'r')
    total = len(x.readlines())
    x.close()
    return total

print('Linhas no arquivo:', contar_linhas('cadastro.txt'))