def main():
    linha = ' '
    for i in range(99, 251, 1):
        linha += str(i) + ' ' + 'bugs no software, pegue um deles e conserte...' + '\n'
    print(f'{linha.strip()}')

if __name__ == "__main__":
    main()       