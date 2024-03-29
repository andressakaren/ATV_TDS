def saldos(valor):
    return round(valor)

def main():
    saldo = float(input('Digite uma quantidade em dinheiro:R$ '))

    print(f'Seu saldo em número interiros é: R$ {saldos(saldo)}.')

if __name__ == '__main__':
    main()