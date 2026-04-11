# 8. Identificação de ano bissexto
# Enunciado:
# Um ano é bissexto se for divisível por 4, mas não por 100, a menos que 
# também seja divisível por 400.
# Leia um ano e use and e or para determinar se ele é bissexto.
# Exiba "Ano bissexto" ou "Ano não bissexto".

ano = int(input("Digite um ano: "))

bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

resultado = bissexto and "Ano bissexto" or "Ano não bissexto"

print(resultado)