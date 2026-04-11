# 4. Compra com desconto
# Enunciado:
# Leia o valor da compra e se o cliente é VIP (True ou False).
# O cliente ganha 10% de desconto se o valor for maior que R$ 100 ou ele for VIP.
# Exiba o valor final com desconto (se aplicável) ou o valor original.

valor = float(input("Digite o valor da compra: "))
vip = input("Cliente é VIP? (True/False): ") == "True"

desconto = (valor > 100 or vip) * 0.10
valor_final = valor - (valor * desconto)

print(f"Valor final: R$ {valor_final:.2f}")