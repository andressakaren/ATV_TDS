def main():
    while True:
        nota = float(input().strip())
        if nota > 10 or nota < 0: 
            print('Nota inválida.')
        else:
            break
    if nota >= 8.5:
        print('A')
    elif nota >= 7:
        print('B')
    elif nota >= 5:
        print('C')
    elif nota >= 4:
        print('D')
    elif nota >= 0:
        print('E')

if __name__ == '__main__':
    main()