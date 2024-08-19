def main():
    num = 0
    soma = 0

    while True:
        num = int(input('Digite um número: ').strip())
        if num == 0: break
        soma += num

    print('A soma de todos os números é: ',soma)

if __name__ == '__main__':
    main()