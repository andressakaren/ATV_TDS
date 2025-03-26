# 5. Faça um programa que leia a altura e o sexo (codificado da seguinte forma:
# 1:feminino 2:masculino) de uma pessoa. Depois faça uma função chamada peso ideal que receba a altura e o sexo via parâmetro e
# que calcule e retorne seu peso ideal, utilizando as seguintes fórmulas:
# - para homens : (72.7 * h) – 58
# - para mulheres : (62.1 * h) – 44.7
# Observação: Altura = h (na fórmula acima).

def peso_ideal(altura, sexo):
    if sexo == 1:
        peso_mulheres = (62.1 * altura) - 44.7
        return round(peso_mulheres, 2)
    if sexo == 2:
        peso_homens = (72.7 * altura) - 58
        return round(peso_homens, 2)


while True:
    try:
        altura = float(input('Digite a altura: '))
        sexo = int(
            input('Digite o sexo, sendo: \n1 - feminino \n2 - masculino \n>'))
        if sexo not in [1, 2]:
            print('Valor inválido!')
            continue

        if sexo == 1:
            print(
                f'O peso ideal para MULHERES baseado na sua altura: {peso_ideal(altura, sexo)}kg')
        elif sexo == 2:
            print(
                f'Peso ideal para HOMENS baseado na sua altura: {peso_ideal(altura, sexo)}kg')

        break
    except:
        print('valor inválido. Digite um valor válido.')
