def main():
    valorQuilo = float(input('')) # R$/Kg
    qtdConsumida = float(input(''))
    valorFinal = valorQuilo * qtdConsumida
    
    print(f'{valorFinal:.2f}')
if __name__ == '__main__':
    main()