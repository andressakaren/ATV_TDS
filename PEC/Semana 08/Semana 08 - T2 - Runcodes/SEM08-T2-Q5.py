def calculo(nota1, nota2, nota3, media_exercicios):
    media_final = (nota1 + (nota2 * 2) + (nota3 * 3) + media_exercicios) / 7
    
    #conceito média final 
    if media_final >= 9.0:
        return (f'{media_final:.2f}\nA\nAprovado')
    if  7.5 <= media_final < 9.0:
        return (f'{media_final:.2f}\nB\nAprovado')
    if 6.0 <= media_final < 7.5:
        return (f'{media_final:.2f}\nC\nAprovado')
    if 4.0 <= media_final < 6.0 :
        return (f'{media_final:.2f}\nD\nReprovado')
    if media_final < 4.0:
        return (f'{media_final:.2f}\nE\nReprovado')

def main():
    matricula = (input()).strip()
    nota1 = float(input())
    nota2 = float(input())
    nota3 = float(input())
    media_exercicios = float(input())
    
    print(f'{matricula}\n{calculo(nota1, nota2, nota3, media_exercicios)}')
    
if __name__ == '__main__':
    main()
    