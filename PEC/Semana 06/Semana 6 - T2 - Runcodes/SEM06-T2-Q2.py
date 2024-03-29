def saldos(valor):
    return round(valor)

def main():
    saldo = float(input())

    print(f'{saldos(saldo)}')

if __name__ == '__main__':
    main()