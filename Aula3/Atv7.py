ano = int(input("Ano de nascimento: "))
sexo = input("Sexo (M/F): ").upper()
deficiencia = input("Possui deficiência? (sim/não): ").lower()

idade = 2026 - ano

if deficiencia == "sim":
    print("Dispensado por condição de saúde")
elif sexo == "F":
    print("Não obrigatório")
else:
    if idade < 18:
        print(f"Faltam {18 - idade} anos para alistamento")
    elif idade == 18:
        print("Aliste-se imediatamente")
    elif idade <= 45:
        print("Já passou do prazo")
    else:
        print("Dispensado por idade")