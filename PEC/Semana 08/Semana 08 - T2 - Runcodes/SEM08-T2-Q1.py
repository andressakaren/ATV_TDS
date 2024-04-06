def e_par(num):
    if num % 2 == 0:
        return num + 5
    else:
        return num + 8

def main():
    num = int(input())
    print(f'{e_par(num)}')
    
if __name__ == '__main__':
    main()