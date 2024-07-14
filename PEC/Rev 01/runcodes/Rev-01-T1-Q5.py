def main():
    custoFabrica = float(input(''))
    # custoCarroNovo = custoFabrica + (porcentagemDist (28%) * custoFabrica) + (imposto(45%) * custoFabrica)
    custoCarroNovo = custoFabrica + (0.28 * custoFabrica) + (0.45 * custoFabrica)
    print(f'R$ {custoCarroNovo:.2f}')
if __name__ == '__main__':
    main()