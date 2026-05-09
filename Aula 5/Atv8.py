class ContaBancaria:

    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito de R${valor:.2f} realizado.')

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R${valor:.2f} realizado.')
        else:
            print('Saldo insuficiente')

    def exibir_saldo(self):
        print(f'Saldo atual: R${self.saldo:.2f}')


conta = ContaBancaria('João')


conta.depositar(500)
conta.sacar(150)
conta.sacar(400)


conta.exibir_saldo()