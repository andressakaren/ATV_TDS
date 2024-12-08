class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo # PRIVADO
        
    # Método PUBLICO para acessar o saldo
    def mostrar_saldo(self):
        return f'Saldo atual: R${self.__saldo:.2f}'
    
    # Método PUBLICO para alterar o saldo
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor do depósito deve ser positivo!')
            
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        else: 
            print('Saldo insuficiente ou valor inválido!')
            
    def __str__(self):
        return f'Titular: {self.titular}\nSaldo atual: R${self.__saldo:.2f}'
            
# crinado o objeto
conta = ContaBancaria('Andressa', 500.0)

print(conta)
# Titular: Andressa
# Saldo atual: R$500.00

print(conta.mostrar_saldo())
# Saldo atual: R$500.00

print(conta.__saldo)
    