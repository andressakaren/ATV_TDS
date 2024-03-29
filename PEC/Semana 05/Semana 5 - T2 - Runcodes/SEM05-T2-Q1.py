def eVogal(caractere):
    return caractere.upper() in 'AEIOU' 
def main():
    caractere = input().strip()
    print(f'{eVogal(caractere)}')
if __name__ == '__main__':
    main()