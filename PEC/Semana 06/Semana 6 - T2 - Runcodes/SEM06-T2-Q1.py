def frases(caracteres):
    return len(caracteres)

def main():
    frase = input().strip()

    print(f'{frases(frase)}')

if __name__ == '__main__':
    main()