# INCOMPLETA

def main():
    linha = ''
    for i in reversed(range(11,100, 11)):
        linha += str(i) + " bugs no software, pegue um deles e conserte...\nTecle \"Ctrl+F5\"\n"
    print(f'{linha.strip()}')
    print(f'Sem erros no software! Está estabilizado!'.strip())

if __name__ == "__main__":
    main()