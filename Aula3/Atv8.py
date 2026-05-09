idade = int(input("Idade: "))
plano = input("Plano (basico/standard/premium): ").lower()

if plano == "basico":
    valor = 100 + idade * 2
elif plano == "standard":
    valor = 150 + idade * 3
elif plano == "premium":
    valor = 200 + idade * 5
else:
    print("Plano inválido")
    exit()

if idade > 60:
    valor *= 1.10

print(f"Valor mensal: R$ {valor:.2f}")