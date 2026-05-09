class Funcionario:
    def __init__(self, nome, cargo, salario_base):
        self.nome = nome
        self.cargo = cargo
        self.salario_base = float(salario_base)

    def aumentar_salario(self, percentual):
        aumento = self.salario_base * (percentual / 100)
        self.salario_base += aumento
        print(f"O salário de {self.nome} foi reajustado em {percentual}%")

    def calcular_bonus(self):
        return self.salario_base * 0.10

    def exibir_dados(self):

        bonus = self.calcular_bonus()
        print("\n--- Dados do Funcionário ---")
        dados = {
            "Nome": self.nome,
            "Cargo": self.cargo,
            "Salário Base": f"R$ {self.salario_base:.2f}",
            "Bônus (10%)": f"R$ {bonus:.2f}",
            "Total": f"R$ {self.salario_base + bonus:.2f}"
        }
        for chave, valor in dados.items():
            print(f"{chave}: {valor}")
        return dados


func1 = Funcionario('Carlos Silva', 'Analista de Sistemas', 5000)


print("Dados Iniciais:")
func1.exibir_dados()

print("\nAplicando aumento...")
func1.aumentar_salario(15)

func1.exibir_dados()