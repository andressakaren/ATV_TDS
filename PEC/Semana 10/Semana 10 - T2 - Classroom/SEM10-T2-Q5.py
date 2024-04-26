def main():
    valor_compra = float(input('Digite o valor da compra: R$ '))
    print(f'O valor da prestação sem juros: ')
    for i in range(1, 25):
        parcela = valor_compra / i
        print(f'{i}x de R$ {parcela:.2f}')
        
if __name__ == "__main__":
    main()