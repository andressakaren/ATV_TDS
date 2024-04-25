# INCOMPLETO

def main():
    linha = ' '
    ultima = ' '
    for i in range(99, 251, 1):
        if i < 250:
            linha += str(i) + ' bugs no software, pegue um deles e conserte...\nTecle “Ctrl+F5”\n'
        else:
            ultima = str(i) + ' bugs no software, pegue um deles e conserte...\nTecle “Ctrl+F5”'
    print(f'{linha.strip()}\n{ultima.strip()}')
    print(f'Vamos fazer mais um café!')

if __name__ == "__main__":
    main()       