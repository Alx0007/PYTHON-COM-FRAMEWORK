
class Carro:
    def __init__(self, marca, modelo):
        self.marca =  marca
        self.modelo =  modelo
        self.__velocidade =  0

    def acelerar(self, valor):
        self.__velocidade += valor
        if self.__velocidade > 200:
            self.__velocidade = 200

    def frear(self, valor):
        self.__velocidade -= valor
        if self.__velocidade < 0:
            self.__velocidade = 0

    @property
    def velocidade(self):
        return self.__velocidade



c  =  Carro('Ferrari', 'Ferrari')
c.acelerar(50)
c.acelerar(300)
c.frear(100)

print(c.velocidade)