def total(preco, quantidade):
    return preco * quantidade


def main():
    preco_maca = float(input())
    preco_banana = float(input())

    total_maca = total(preco_maca, 3)
    total_banana = total(preco_banana, 2)

    total_geral = total_maca + total_banana

    print(f'{total_geral:.2f}')



if __name__ == '__main__':
    main()