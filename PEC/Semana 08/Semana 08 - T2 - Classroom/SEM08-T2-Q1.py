def e_par(num):
    if num % 2 == 0:
        return num + 5
    else:
        return num + 8

def main():
    num = int(input('Digite um número: '))
    print(f'O número digitado foi {num} e o resultado da soma é: {e_par(num)}')
    
if __name__ == '__main__':
    main()
