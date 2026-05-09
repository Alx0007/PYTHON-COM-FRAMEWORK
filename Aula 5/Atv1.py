x = open('cadastro.txt', 'a')
while True:
    nome = input('Nome (ou sair): ')
    if nome.lower() == 'sair':
        break
    idade = input('Idade: ')
    x.write(nome + ',' + idade + '\n')
x.close()