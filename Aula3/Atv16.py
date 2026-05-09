n = int(input("Quantos termos da sequência de Fibonacci você quer ver? "))

a = 0
b = 1

for i in range(n):
    print(a)
    proximo = a + b
    a = b
    b = proximo