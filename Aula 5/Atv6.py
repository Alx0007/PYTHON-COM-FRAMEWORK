# Crie uma classe Pessoa com os atributos nome e idade. Adicione um método apresentar() que exiba "Olá, meu nome é [nome] e tenho [idade] anos." Crie duas pessoas diferentes e chame o método.


# criei a classe
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade  = idade
# criei o método
    def apresentar(self):
        print(f'Olá, meu nome é {self.nome}, eu tenho {self.idade}')
# instaciei a classe
pessoa1 =  Pessoa('Kaio',20)
pessoa2 =  Pessoa('Maria',22)
# usei o método na instancia 
pessoa1.apresentar()
pessoa2.apresentar()