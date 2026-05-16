class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome =  nome
        self.cargo = cargo
        self.salario = salario




    def __len__(self):
        return len(self.nome)
    



f  =  Funcionario('diogo', 'dev', '5000')
print(f.__len__())    