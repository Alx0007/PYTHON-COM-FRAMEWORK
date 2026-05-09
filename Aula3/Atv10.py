valor = int(input("Valor do saque: "))

if valor < 10 or valor > 1000 or valor % 5 != 0:
    print("Valor inválido")
else:
    notas50 = valor // 50
    valor %= 50

    notas20 = valor // 20
    valor %= 20

    notas10 = valor // 10
    valor %= 10

    notas5 = valor // 5

    print(f"50: {notas50}")
    print(f"20: {notas20}")
    print(f"10: {notas10}")
    print(f"5: {notas5}")