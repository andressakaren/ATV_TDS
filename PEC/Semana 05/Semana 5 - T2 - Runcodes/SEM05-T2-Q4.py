def eNum(caractere):
    return caractere in '0123456789' 

def eLetra(caractere):
    return 'A' <= caractere.upper() <= 'Z' 

def comparacao (caractere):
    return eLetra(caractere) or eNum(caractere)

def main():
    caractere = input().strip()
    print(f'{comparacao(caractere)}')
    
if __name__ == '__main__':
    main()