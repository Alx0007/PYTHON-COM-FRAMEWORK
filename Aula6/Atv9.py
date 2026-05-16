class Estatistica: 

    soma =  0
    contagem = 0


    @classmethod
    def adcionar(cls, valor):
        cls.soma  += valor
        cls.contagem += 1


    @classmethod
    def calcular_media(cls):
        if cls.contagem == 0:
            return 0
        return cls.soma/cls.contagem
    


Estatistica.adcionar(10)
Estatistica.adcionar(5)
Estatistica.adcionar(2)


print(Estatistica.calcular_media())