def main():
    soma = 0
        
    for i in range(100):
        i = int(input('Digite um número: '))
        soma += i
        
    media = soma / 100
    print(f'A média de todos os valores digitados é: {media:.2f}.')
        
if __name__ == "__main__":
    main()