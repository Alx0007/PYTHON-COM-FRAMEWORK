class Retangulo:

    def __init__(self):
        self.altura = 3
        self.largura = 5

    def calcular_area(self):
        return self.largura * self.altura

    def calcular_perimetro(self):
        return 2*(self.largura+self.altura)


retangulo = Retangulo()

area = retangulo.calcular_area()

perimetro = retangulo.calcular_perimetro()

print(area)
print(perimetro)