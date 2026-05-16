class Calculadora:


    @staticmethod
    def soma(a,b):
        return a + b
    
    @staticmethod
    def subtrair(a,b):
        return a - b


    @staticmethod
    def mult(a,b):
        return a * b
    
    @staticmethod
    def div(a,b):
        return a / b
    
print(Calculadora.div(100,200))