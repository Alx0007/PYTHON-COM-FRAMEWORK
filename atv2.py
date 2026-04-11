# 2. Classificação de peso ideal
# Enunciado:
# Leia o peso (kg) e a altura (m) de uma pessoa. Calcule o IMC (peso / altura**2).
# Uma pessoa está com peso normal se o IMC estiver entre 18.5 e 24.9 (inclusive).
# Use operadores lógicos para verificar se o IMC está nessa faixa e exiba 
# "Peso normal" ou "Fora da faixa".


peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

calculo = peso / (altura ** 2)

calculo2 = (calculo>= 18.5 and calculo<=24.9 ) and "Peso normal" or "Fora da faixa"

print('resultado:', calculo)
print(calculo2)
