def menor_diferenca(n1, n2, n3):
    if abs(n1 - n2) < abs(n1 - n3):
        return abs(n1 - n2)
    else:
        return abs(n1 - n3)


def main():
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    
    print(f'{menor_diferenca(n1, n2, n3)}')
    
if __name__ == '__main__':
    main()