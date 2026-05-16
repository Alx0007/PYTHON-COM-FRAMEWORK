class ContaBancaria:
    def __init__(self):
        self.__saldo = 0


    def teste(self):
        return self.__saldo    
        
    def depositar(self, valor):
        self.__saldo += valor
        
    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print('Saldo insuficiente...')
        


conta  =  ContaBancaria()
conta.depositar(1000)
conta.sacar(500)


print(conta.__saldo)


