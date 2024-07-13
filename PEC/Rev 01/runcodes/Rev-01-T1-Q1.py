def main():
    precoProduto = float(input(''))
    valorPago = float(input(''))
    troco = valorPago - precoProduto
    if troco >= 0:
        print(f'{troco:.2f}')
    else: 
        print('Pagamento Insuficiente')
if __name__ == '__main__':
    main()