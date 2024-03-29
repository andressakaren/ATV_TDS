def eLetra(caractere):
    return 'A' <= caractere.upper() <= 'Z' 

def main():
    caractere = input('Digite um caractere? ').strip()
    print(f'Esse caractere é uma Letra? {eLetra(caractere)}.')
    
if __name__ == '__main__':
    main()