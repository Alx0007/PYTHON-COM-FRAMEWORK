
class Aluno:
    def __init__(self, nome, matricula):
        self.nome  = nome
        self.matricula =  matricula 
        self.__notas = []

    def adcionar_notas(self, nota):
        if 0 <= nota <= 10 :
            self.__notas.append(nota)
            
    def calcular_media(self):
        if len(self.__notas) == 0:
            return 0
        return sum(self.__notas) / len(self.__notas)
    
    def situacao(self):
        media  =  self.calcular_media()
        if media >= 7:
            return 'Aprovado'
        elif media >= 5:
            return 'Recuperação'
        else:
            return 'Reprovado'

aluno1 = Aluno('Ana', '1')
aluno2 = Aluno('Julia', '2')

aluno1.adcionar_notas(8)
aluno1.adcionar_notas(5)
aluno1.adcionar_notas(10)

aluno2.adcionar_notas(1)
aluno2.adcionar_notas(2.5)
aluno2.adcionar_notas(10)

print('Média',aluno1.nome ,aluno1.calcular_media())
print('Média',aluno2.nome ,aluno2.calcular_media())

print(aluno1.situacao())
print(aluno2.situacao())