def terceira_nota(media, nota3):
    
    if nota3 > 8:
        media = media + 1

    if media > 10:
        media = 10
        
    return media
    
def main():
    nota1 = float(input())
    nota2 = float(input())
    nota3 = float(input())
    
    media = (nota1 + nota2 + nota3) / 3
    
    print(f'{terceira_nota(media, nota3):.2f}')
    
if __name__ == '__main__':
    main()