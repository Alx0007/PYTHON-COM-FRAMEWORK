class Calculadora:
    @staticmethod
    def somar(a, b):
        resultado = a + b
        print(f"Soma: {a} + {b} = {resultado}")
        return resultado

    @staticmethod
    def subtrair(a, b):
        resultado = a - b
        print(f"Subtração: {a} - {b} = {resultado}")
        return resultado

    @staticmethod
    def multiplicar(a, b):
        resultado = a * b
        print(f"Multiplicação: {a} * {b} = {resultado}")
        return resultado

    @staticmethod
    def dividir(a, b):
        if b == 0:
            print("Erro: Divisão por zero")
            return None
        resultado = a / b
        print(f"Divisão: {a} / {b} = {resultado}")
        return resultado

Calculadora.somar(10, 5)
Calculadora.subtrair(20, 8)
Calculadora.multiplicar(4, 3)
Calculadora.dividir(50, 2)