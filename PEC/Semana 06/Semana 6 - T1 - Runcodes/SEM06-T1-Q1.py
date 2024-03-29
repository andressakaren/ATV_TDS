def qnts_caracteres(nome):
    return len(nome)

def main():
    nome = str(input()).strip()
    print(f'{qnts_caracteres(nome)}')
    
if __name__ == '__main__':
    main()

