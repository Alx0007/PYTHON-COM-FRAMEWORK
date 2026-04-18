print("Programa com dois números")

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

print("Soma:", n1 + n2)
print("Subtração:", n1 - n2)
print("Multiplicação:", n1 * n2)
print("Divisão:", n1 / n2)

print("Os números são iguais?", n1 == n2)
print("O primeiro número é maior que o segundo?", n1 > n2)
print("Pelo menos um dos números é maior que 10?", n1 or n2 > 10)