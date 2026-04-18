print('E-COMMERCE X')
login = input('Login: ')

produtos = ['hd', 'ram', 'teclado', 'mouse', 'pendrive']
valores = [1000, 90.20, 455.45, 585.12, 454.45]

print('----' * 10)

print(f'''
0 - {produtos[0]} R$ {valores[0]}
1 - {produtos[1]} R$ {valores[1]}
2 - {produtos[2]} R$ {valores[2]}
3 - {produtos[3]} R$ {valores[3]}
4 - {produtos[4]} R$ {valores[4]}
''')

prod1 = int(input('Produto: '))
prod2 = int(input('Produto: '))
prod3 = int(input('Produto: '))

carrinho = []
valor = []

carrinho.append(produtos[prod1])
print('No seu carrinho:', carrinho)

carrinho.append(produtos[prod2])
print('No seu carrinho:', carrinho)

carrinho.append(produtos[prod3])
print('No seu carrinho:', carrinho)

valor.extend([valores[prod1], valores[prod2], valores[prod3]])

soma = sum(valor)

print('Carrinho final:', carrinho)
print('Total: R$', soma)

print('----' * 10)
print('LISTA DE NOMES')

nomes = []

nomes.append('Lucas')
nomes.append('Maria')
nomes.append('Joao')

print('Lista com 3 nomes:', nomes)

nomes.remove('Joao')
nomes.remove('Maria')

print('Lista depois de remover os 2 ultimos nomes:', nomes)