class Produto:

    def __init__(self, nome, preco, quantidade_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque

    def total_estoque(self):
        return self.preco * self.quantidade_estoque

    def adicionar_estoque(self, quantidade):
        self.quantidade_estoque += quantidade
        print(f'{quantidade} itens adicionados ao estoque.')

    def remover_estoque(self, quantidade):
        if quantidade <= self.quantidade_estoque:
            self.quantidade_estoque -= quantidade
            print(f'{quantidade} itens removidos do estoque.')
        else:
            print('Estoque insuficiente.')


produto = Produto('Notebook', 3500, 10)


produto.adicionar_estoque(5)
produto.remover_estoque(8)
produto.remover_estoque(20)

print(f'Valor total do estoque: R${produto.total_estoque():.2f}')