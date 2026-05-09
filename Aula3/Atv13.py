soma = 0
quantidade = 0

while True:
    nota = float(input("Digite uma nota de 0 a 10 (-1 para encerrar): "))

    if nota == -1:
        break

    if nota < 0 or nota > 10:
        print("Nota inválida, tente novamente.")
        continue

    soma += nota
    quantidade += 1

if quantidade > 0:
    media = soma / quantidade
    print(f"Média das notas: {media:.2f}")
else:
    print("Nenhuma nota válida foi digitada.")