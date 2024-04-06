def calculo_imc(m, h):
    imc = m / (h*h)
    
    if imc < 18.5:
        return (f'{imc:.2f}\nAbaixo do peso')
    elif 18.5 <= imc < 25:
        return (f'{imc:.2f}\nPeso normal')
    elif 25 <= imc < 30:
        return (f'{imc:.2f}\nSobrepeso')
    elif 30 <= imc < 35:
        return (f'{imc:.2f}\nObeso leve')
    elif 35 <= imc < 40:
        return (f'{imc:.2f}\nObeso moderado')
    elif 40 <= imc < 45:
        return (f'{imc:.2f}\nObeso mórbido')

def main():
    m = float(input())
    h = float(input())
    
    print(f'{calculo_imc(m, h)}')
    
if __name__ == '__main__':
    main()