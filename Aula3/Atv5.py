j1 = input("Jogador 1: ").lower()
j2 = input("Jogador 2: ").lower()

if j1 == j2:
    print("Empate")
elif (j1 == "pedra" and j2 == "tesoura") or \
     (j1 == "tesoura" and j2 == "papel") or \
     (j1 == "papel" and j2 == "pedra"):
    print("Jogador 1 venceu")
else:
    print("Jogador 2 venceu")