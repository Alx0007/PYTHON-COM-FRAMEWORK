
class Produto:
    def __init__(self, nome, preco, quantidade):
        self._nome = nome
        self._preco = preco
        self._quantidade  =  quantidade
        
    @property
    def nome(self):
        return self._nome
    
    @property
    def preco(self):
        return self._preco
    
    @property
    def quantidade(self):
         return self._quantidade
    
    def aplicar_desconto(self, percentual):
        desconto = self._preco * percentual
        novo = self._preco  - desconto
        if self._preco >= 0:
            self._preco = novo
            
            

p =  Produto('HD', 100.0,1)
p.aplicar_desconto(0.10)
print(p)
print(p.nome, p.preco)        
    