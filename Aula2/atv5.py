# 5. Elegibilidade para doação de sangue
# Enunciado:
# Leia a idade e o peso.
# Para doar sangue, a pessoa deve ter entre 16 e 69 anos (inclusive) e 
# pesar pelo menos 50 kg.
# Use and para verificar ambos os critérios e informe se a pessoa pode doar.

peso = float(input('Digite seu peso: '))
idade= int(input('Digite sua idade: '))



verificar = (peso>= 50 and idade >=16 and idade <= 69 ) and "Pode doar" or "Não pode doar"

print(verificar)
