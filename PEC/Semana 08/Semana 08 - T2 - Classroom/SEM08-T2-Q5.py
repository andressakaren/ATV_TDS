def calculo(nota1, nota2, nota3, media_exercicios):
    media_final = (nota1 + (nota2 * 2) + (nota3 * 3) + media_exercicios) / 7
    
    #conceito média final 
    if media_final >= 9.0:
        return (f'Média Final: {media_final:.2f}\nConceito: A\nAprovado')
    if  7.5 <= media_final < 9.0:
        return (f'Média Final: {media_final:.2f}\nConceito: B\nAprovado')
    if 6.0 <= media_final < 7.5:
        return (f'Média Final: {media_final:.2f}\nConceito: C\nAprovado')
    if 4.0 <= media_final < 6.0 :
        return (f'Média Final: {media_final:.2f}\nConceito: D\nReprovado')
    if media_final < 4.0:
        return (f'Média Final: {media_final:.2f}\nConceito: E\nReprovado')

def main():
    matricula = (input()).strip()
    nota1 = float(input())
    nota2 = float(input())
    nota3 = float(input())
    media_exercicios = float(input())
    
    print(f'''Resultado:
Matricula: {matricula}\n{calculo(nota1, nota2, nota3, media_exercicios)}
          
          
Legenda: 
A >= 9.0
B >= 7.5 e < 9.0
C >= 6.0 e < 7.5
D >= 4.0 e < 6.0
E < 4.0

Aprovado - A, B ou C
Reprovado - D ou E''')
    
if __name__ == '__main__':
    main()
    
