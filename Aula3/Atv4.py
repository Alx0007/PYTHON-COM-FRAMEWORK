salario = float(input("Salário bruto: "))

inss = salario * 0.11
if inss > 1500:
    inss = 1500

base = salario - inss

if salario <= 2500:
    irrf = 0
elif salario <= 3500:
    irrf = (salario - 2500) * 0.075
elif salario <= 5000:
    irrf = (salario - 3500) * 0.15
else:
    irrf = (salario - 5000) * 0.275

liquido = salario - inss - irrf

print(f"Salário líquido: R$ {liquido:.2f}")