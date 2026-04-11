# 9. Faixa etária
# Enunciado:
# Leia a idade e classifique:

# "Criança" se idade < 12

# "Adolescente" se 12 ≤ idade ≤ 17

# "Adulto" se idade ≥ 18
# Use and e or para definir os intervalos e exiba a classificação.

idade = int(input('Digite sua idade: '))

v = (idade < 12 and "Criança") or (idade <= 12 and idade <= 17 and 'Adolescente') or (idade >= 18 and 'Adulto')

print(v)
