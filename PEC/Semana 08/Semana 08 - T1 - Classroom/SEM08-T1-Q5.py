
def calculo_imc(m, h):
    imc = m / (h*h)
    
    if imc < 18.5:
        return (f'IMC: {imc:.2f}\nClassificação: Abaixo do peso')
    elif 18.5 <= imc < 25:
        return (f'IMC: {imc:.2f}\nClassificação: Peso normal')
    elif 25 <= imc < 30:
        return (f'IMC: {imc:.2f}\nClassificação: Sobrepeso')
    elif 30 <= imc < 35:
        return (f'IMC: {imc:.2f}\nClassificação: Obeso leve')
    elif 35 <= imc < 40:
        return (f'IMC: {imc:.2f}\nClassificação: Obeso moderado')
    elif 40 <= imc < 45:
        return (f'IMC: {imc:.2f}\nClassificação: Obeso mórbido')

def main():
    m = float(input('Digite seu peso: '))
    h = float(input('Digite sua altura: '))
    
    print(f'''
Valores referência:

< 18,5	Abaixo do peso
< 25	Peso normal
< 30	Sobrepeso
< 35	Obeso leve
< 40	Obeso moderado
>=40	Obeso mórbido

Seu resultado:
{calculo_imc(m, h)}''')
    
if __name__ == '__main__':
    main()
