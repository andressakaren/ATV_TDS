def total(preco, quantidade):
    return preco * quantidade

def main():
    preco_maca = float(input('Digite o valor da maçã: R$ '))
    preco_banana = float(input('Digite o valor da banana: R$ '))

    total_maca = total(preco_maca, 3)
    total_banana = total(preco_banana, 2)

    total_geral = total_maca + total_banana

    print(f'O total da compra de 3 maçãs e 2 bananas é: {total_geral:.2f}')

if __name__ == '__main__':
    main()