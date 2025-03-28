# 4. Escreva um programa para ler as notas das duas avaliações de um aluno no semestre. Faça um procedimento que receba as duas
# notas por parâmetro e calcule e escreva a média semestral e a mensagem “PARABÉNS! Você foi aprovado!” somente se o aluno
# foi aprovado (considere 6.0 a média mínima para aprovação).

def media_semestral(n1, n2):
    media = (n1 + n2) / 2
    return round(media, 2)


while True:
    try:
        n1 = float(input('Digite a primeira nota: '))
        n2 = float(input('Digite a segunda nota: '))
        print(f'Média: {media_semestral(n1, n2)}')
        if media_semestral(n1, n2) >= 6:
            print('PARABÉNS! Você foi aprovado')
        break
    except:
        print('valor inválido. Digite uma nota válida.')
