def dobro(deposito, taxa):
    i = 1
    capital = deposito
    while True:
        capital = deposito * (taxa/100 + 1) ** i
        if capital >= deposito * 2: break
        i+=1
    return i

def main():
    deposito = float(input('Digite o valor do deposito: ').strip())
    taxa = float(input('Digite o valor da taxa: ').strip())
    print(f'O valor vai dobrar em {dobro(deposito, taxa)} anos.')

if __name__ == '__main__':
    main()