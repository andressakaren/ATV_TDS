// 4) Adicione na classe da questão anterior o método para realizar transferência entre contas, que recebe como parâmetros uma conta e o valor a ser transferido.

class ContaBancaria {
    constructor(num_conta, nome, saldo) {
        this.num_conta = num_conta;
        this.nome = nome;
        this.saldo = saldo;
    }

    depositar(valor) {
        if (valor > 0) {
            this.saldo += valor;
            console.log(`Depósito de R$ ${valor.toFixed(2)} realizado.\nNovo saldo: R$ ${(this.saldo).toFixed(2)}`);
        } else {
            console.log('Deposite um valor válido'); 
        }
    }

    sacar(valor) {
        if (valor <= this.saldo) {
            this.saldo -= valor
            console.log(`Saque de R$ ${valor} realizado.\nNovo saldo: R$ ${this.saldo}`)
        } else {
            console.log('Saldo insuficiente')
        }
    }

    getSaldo() {
        return `Saldo atual: R$${this.saldo.toFixed(2)}`; 
    }

    //realizar transferência entre contas, que recebe como parâmetros uma conta e o valor a ser transferido.
    tranferencia(num_conta_transferencia, valor) {
        if (valor <= 0) {
            console.log(`O valor de transferencia deve ser maior que zero!`)
        } else if (valor > this.saldo) {
            console.log(`Saldo insuficiente. Seu saldo atual: R$ ${this.saldo.toFixed(2)}`)
        } else {
            this.saldo -= valor
            console.log(`Tranferencia de R$ ${valor.toFixed(2)} realizada para a conta ${num_conta_transferencia}`)
        }
    }
}

const conta1 = new ContaBancaria('123', 'Andressa', 50)
console.log(conta1.getSaldo())
conta1.depositar(100)
conta1.sacar(25)
conta1.tranferencia('57190-8', 50)
console.log(conta1.getSaldo())
conta1.tranferencia('57190-8', 0) //O valor de transferencia deve ser maior que zero!     
conta1.tranferencia('57190-8', 100) //Saldo insuficiente. Seu saldo atual: R$ 75.00

