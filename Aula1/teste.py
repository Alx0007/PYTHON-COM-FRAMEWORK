print('Calculo de nota bimestral')

n1= float(input("Digite a primeira nota: "))
n2= float(input("Digite a segunda nota: "))
n3= float(input("Digite a terceira nota: "))
n4= float(input("Digite a quarta nota: "))

total = n1+n2+n3+n4
final = total/4

print("nota final: ",final)

if final >= 7.0:
 print("Aprovado")
else:
 print("Reprovado")