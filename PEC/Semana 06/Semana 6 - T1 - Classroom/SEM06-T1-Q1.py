def qnts_caracteres(nome):
    return len(nome)

def main():
    nome = str(input('Digite um nome: ')).strip()
    
    print(f'O nome {nome} tem {qnts_caracteres(nome)} caracteres.')
    
if __name__ == '__main__':
    main()
