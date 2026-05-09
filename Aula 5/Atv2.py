x = open('cadastro.txt', 'r')
for linha in x:
    dados = linha.strip().split(',')
    print('Nome:', dados[0], ', Idade:', dados[1])
x.close()