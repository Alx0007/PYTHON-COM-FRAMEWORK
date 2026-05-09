origem = input('Arquivo origem: ')
destino = input('Arquivo destino: ')

o = open(origem, 'r')
d = open(destino, 'w')
d.write(o.read())

o.close()
d.close()