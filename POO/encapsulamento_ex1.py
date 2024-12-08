class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo
        
    # Método PUBLICO para acessar o saldo
    def mostrar_saldo(self):
        return f'Saldo atual: R${self._saldo:.2f}'
    
    # Método PUBLICO para alterar o saldo
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
        else:
            print('O valor do depósito deve ser positivo!')
            
    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
        else: 
            print('Saldo insuficiente ou valor inválido!')
            
    def __str__(self):
        return f'Titular: {self.titular}\nSaldo atual: R${self._saldo:.2f}'
            
# crinado o objeto
conta = ContaBancaria('Andressa', 500.0)

print(conta)
# Titular: Andressa
# Saldo atual: R$500.00

print(conta.mostrar_saldo())
# Saldo atual: R$500.00

conta.depositar(100)
print(conta.mostrar_saldo())
# Saldo atual: R$600.00

conta.sacar(200)
print(conta.mostrar_saldo())
# Saldo atual: R$400.00

# print(conta._saldo)
# 400.0
# tem como acessar diteramente o _saldo, não deve, mas o _ não impede o acesso, diferente do __ que só permite o acesso indiretamente (encapsulamento_ex2.py)