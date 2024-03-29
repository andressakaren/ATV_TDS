def eLetra(caractere):
    return 'A' <= caractere.upper() <= 'Z' 

def main():
    caractere = input().strip()
    print(f'{eLetra(caractere)}')
    
if __name__ == '__main__':
    main()