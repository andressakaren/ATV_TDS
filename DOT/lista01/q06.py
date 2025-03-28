# Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm). Faça um procedimento
# que receba como parâmetro o número de lados e a medida do lado deste polígono e calcule e imprima o seguinte:
# - Se o número de lados for igual a 3, escrever TRIÂNGULO e o valor do seu perímetro.
# - Se o número de lados for igual a 4, escrever QUADRADO e o valor da sua área.
# - Se o número de lados for igual a 5, escrever PENTÁGONO.

def calc_perimetro(l):
    return round(l * 3, 2)
    
def calc_area(l):
    return round(l ** 2, 2)

    
while True:
    try:
        numero_lados = int(input('Digite o NUMERO de lados do polígono, 3, 4 ou 5: '))
        
        if numero_lados not in [3, 4, 5]:
            print('Numero de lados inválido!')
            continue
        
        medida_lado = float(input('Digite a MEDIDA de um dos lados, em cm: \n'))

        if numero_lados == 3:
            print(f'TRIÂNGULO\nPerímetro: {calc_perimetro(medida_lado)} cm')
        elif numero_lados == 4:
                print(f'QUADRADO\nÁrea: {calc_area(medida_lado)} cm')
        elif numero_lados == 5:
                print(f'PENTÁGONO')
        break
    
    except:
        print('valor inválido. Digite um valor válido.')
