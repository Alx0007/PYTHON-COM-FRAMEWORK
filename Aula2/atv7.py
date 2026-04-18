# 7. Aprovação em duas disciplinas
# Enunciado:
# Leia as notas de Matemática e Português.
# O aluno é aprovado se ambas as notas forem maiores ou iguais a 6.
# Use and para verificar e exiba "Aprovado" ou "Reprovado".

nm = float(input('Digite a nota de matemática: '))
np = float(input('Digite a nota de português: '))

v = nm >= 6 and np >= 6 and "Aprovado" or "Reprovado"

print(v)
