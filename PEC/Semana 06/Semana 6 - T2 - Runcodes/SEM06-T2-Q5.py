# Você sabia que os pinguins usam jaquetas devido ao frio na Antártida? Vamos ajudá-los a converter temperaturas!
# Escreva um programa que leia uma temperatura em Celsius e mostre o resultado em Fahrenheit. Lembre-se:
# Fahrenheit = (Celsius x (9 / 5)) + 32

def convert_(temperatura):
    return (temperatura * (9 / 5)) + 32

def main():
    temperatura = float(input())
    print(f'{convert_(temperatura):.2f}')
    
if __name__ == '__main__':
    main()
    