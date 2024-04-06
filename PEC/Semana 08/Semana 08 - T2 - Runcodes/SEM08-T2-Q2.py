def soma(num):
    # numero ENTRE 0 e 100.000
    if 0 < num < 100000:
        u = num % 10
        num = num // 10 
        
        d = num % 10
        num = num // 10
        
        c = num % 10
        num = num // 10
        
        um = num % 10
        num = num // 10
        
        dm = num % 10
        num = num // 10
        
        cm = num % 10
        num = num // 10
        
        total = u + d + c + um + dm + cm
        
        return total
    else: 
        return -1

def main():
    num = int(input())
    print(f'{soma(num)}')
    
if __name__ == '__main__':
    main()