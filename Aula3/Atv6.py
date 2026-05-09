n1 = float(input("N1: "))
n2 = float(input("N2: "))

media = (n1 + n2) / 2

if media >= 7:
    print("Aprovado")
elif media < 4:
    print("Reprovado")
else:
    nr = float(input("Nota de recuperação: "))
    media_final = (media + nr) / 2
    if media_final >= 5:
        print("Aprovado")
    else:
        print("Reprovado")