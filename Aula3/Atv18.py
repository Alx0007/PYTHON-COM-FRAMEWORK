from datetime import datetime

while True:
    print("\nMENU")
    print("1 - Exibir mensagem")
    print("2 - Exibir data/hora atual")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Olá!")
    elif opcao == "2":
        print("Data e hora atual:", datetime.now())
    elif opcao == "3":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida.")