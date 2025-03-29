// 3) Implemente uma classe chamada “ContaBancaria” que possua atributos para armazenar o número da conta, nome do titular e saldo. Adicione métodos para realizar depósitos e saques que recebem como parâmetro o valor.


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
}

const conta1 = new ContaBancaria('123', 'Andressa', 50)
console.log(conta1.saldo)
conta1.depositar(50)
console.log(conta1.saldo)
// conta1.depositar(0) // Deposite um valor válido
conta1.sacar(50)
conta1.sacar(100) // Saldo insuficiente
conta1.saldo