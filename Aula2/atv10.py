# 10. Sistema de alerta de temperatura e umidade
# Enunciado:
# Leia a temperatura (°C) e a umidade (%).
# Dispare um alerta se temperatura > 35 ou umidade > 70.
# Caso contrário, exiba "Condições normais".
# Use or para combinar as condições.

temp = float(input('Digite a temperatua (°C): '))
umi = float(input('Digite a umidade (%): '))

v = (temp > 35 and "Alerta" ) or (umi > 70 and "Alerta") or "Condições normais"

print(v)