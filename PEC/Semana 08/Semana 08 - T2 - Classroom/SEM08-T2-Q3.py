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
    num = int(input('Digite um número: '))
    print(f'''Resultado: {se(num)}

*Legenda:        
• FIZZ se o número é divisível por três;
• BUZZ se o número é divisível por cinco;
• FIZZBUZZ se o número é divisível por três e por cinco ao mesmo tempo.
• O próprio número caso não seja divisível por três ou por cinco.''')
    
if __name__ == '__main__':
    main()
