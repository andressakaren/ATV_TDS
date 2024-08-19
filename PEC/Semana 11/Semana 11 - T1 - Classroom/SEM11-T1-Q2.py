def main():
    num = 0
    contador = 0
    soma = 0

    while True:
        num = int(input('Digite um número: ').strip())
        if num == 0: break
        soma += num
        contador += 1

    print(f'A média aritmética de todos os números é: {soma/contador:.2f}')

if __name__ == '__main__':
    main()