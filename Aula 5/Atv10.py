class Aluno:

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

    def situacao(self):
        media = self.calcular_media()

        if media >= 7:
            return "Aprovado"
        elif media >= 5:
            return "Recuperação"
        else:
            return "Reprovado"



aluno = Aluno("Maria", 123)

aluno.adicionar_nota(8)
aluno.adicionar_nota(6)
aluno.adicionar_nota(7)

print(f"Média: {aluno.calcular_media():.2f}")
print(f"Situação: {aluno.situacao()}")