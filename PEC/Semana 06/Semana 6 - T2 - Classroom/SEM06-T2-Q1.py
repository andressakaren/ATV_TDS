def frases(caracteres):
    return len(caracteres)

def main():
    frase = input('Digite uma frase: ').strip()

    print(f'O número de caracteres nessa frase é: {frases(frase)}.')

if __name__ == '__main__':
    main()