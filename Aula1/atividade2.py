valor = float(input("Digite o valor do produto: "))

desconto = valor * 0.10
final = valor - desconto

print("Valor com desconto:", final)

print("Valor final é maior que 100?", final > 100)
print("Produto ficou barato (menor que 50)?", final < 50)