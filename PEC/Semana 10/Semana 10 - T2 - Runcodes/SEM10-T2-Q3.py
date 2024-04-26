# INCOMPLETA

def main():
    linha = ''
    for i in range(99, 251, 7):
        linha += str(i) + " bugs no software, pegue um deles e conserte...\nTecle \"Ctrl+F5\"\n"
    print(f'{linha.strip()}')
    print(f'Vamos fazer mais um café!')

if __name__ == "__main__":
    main() 