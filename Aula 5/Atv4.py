arquivo = input('Nome do arquivo: ')
palavra = input('Palavra: ').lower()

x = open(arquivo, 'r')
conteudo = x.read().lower()
print('Aparece:', conteudo.count(palavra), 'vezes')
x.close()