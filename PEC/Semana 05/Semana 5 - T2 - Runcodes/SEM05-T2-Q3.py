def eVogal(caractere):
    return caractere.upper() in 'AEIOU' 

def eLetra(caractere):
    return 'A' <= caractere.upper() <= 'Z' 

def comparacao (caractere):
    return eLetra(caractere) and not eVogal(caractere)

def main():
    caractere = input().strip()
    print(f'{comparacao(caractere)}')
    
if __name__ == '__main__':
    main()