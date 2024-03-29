def codigo_numerico(caractere):
    return ord(caractere)
def main():
    caractere = input()
    print(f'{codigo_numerico(caractere)}')
if __name__ == '__main__':
    main()
    