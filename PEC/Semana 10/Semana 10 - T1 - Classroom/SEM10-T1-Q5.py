def main():
    maior = 0
    
    for i in range(100):
        i = int(input('Digite um número: '))
        if i > maior:
            maior = i
    print(f'O maior número dentre os digitados é: {maior}')
    
if __name__ == "__main__":
    main()