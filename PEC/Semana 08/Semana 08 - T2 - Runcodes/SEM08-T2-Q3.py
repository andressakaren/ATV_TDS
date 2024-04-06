def se(num):
    if num > 0 and num % 3 == 0 and num % 5 == 0:
            return (f'FIZZBUZZ')
    if num > 0 and num % 3 == 0 or num % 5 == 0:
        if num % 3 == 0:
            return (f'FIZZ')
        else:
            return (f'BUZZ')
    else:
        return num

def main():
    num = int(input())
    print(f'{se(num)}')
    
if __name__ == '__main__':
    main()