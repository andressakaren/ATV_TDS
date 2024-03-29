def terceira_nota(media, nota3):
    
    if nota3 > 8:
        media += 1

    if media > 10:
        media = 10
        
    return media
    
def main():
    nota1 = float(input('Digite o valor da sua primeira nota: '))
    nota2 = float(input('Digite o valor da sua segunda nota: '))
    nota3 = float(input('Digite o valor da sua terceira nota: '))
    
    media = (nota1 + nota2 + nota3) / 3
    
    print(f'A sua média final é: {terceira_nota(media, nota3):.2f}!!')
    
if __name__ == '__main__':
    main()