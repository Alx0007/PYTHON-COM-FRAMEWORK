dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

bissexto = (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)

if mes < 1 or mes > 12:
    print("Data inválida")
else:
    if mes in [1,3,5,7,8,10,12]:
        valido = dia <= 31
    elif mes in [4,6,9,11]:
        valido = dia <= 30
    else:
        if bissexto:
            valido = dia <= 29
        else:
            valido = dia <= 28
    
    if dia < 1 or not valido:
        print("Data inválida")
    else:
        print("Data válida")