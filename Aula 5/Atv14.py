class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0

    def acelerar(self, valor):
        self.velocidade += valor
        if self.velocidade > 200:
            self.velocidade = 200
        print(f"Acelerando! Velocidade atual: {self.velocidade} km/h")

    def frear(self, valor):
        self.velocidade -= valor
        if self.velocidade < 0:
            self.velocidade = 0
        print(f"Freando! Velocidade atual: {self.velocidade} km/h")

    def velocidade_atual(self):
        print(f"Painel: {self.velocidade} km/h")
        return self.velocidade

meu_carro = Carro("Porsche", "911 Carrera")

meu_carro.acelerar(80)
meu_carro.acelerar(150)
meu_carro.velocidade_atual()
meu_carro.frear(100)
meu_carro.frear(200)
meu_carro.velocidade_atual()