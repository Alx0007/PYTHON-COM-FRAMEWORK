class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome  =  nome 
        self.cargo =  cargo
        self._salario_base =  salario

    def aumentar_salario(self, percentual):
        self._salario_base += self._salario_base * percentual / 100
        return self._salario_base
    
    def calcular_bonus(self):
        return self._salario_base * 0.10

    @property
    def salario(self):
        return self._salario_base

salario = float(input('Salario: '))
f  =  Funcionario('Ana', 'DEv', salario)
aumento = f.aumentar_salario(0.10)
bonus = f.calcular_bonus()           

print(aumento + bonus )    