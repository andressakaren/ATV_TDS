# Fahrenheit = (Celsius x (9 / 5)) + 32

def convert_(temperatura):
    return (temperatura * (9 / 5)) + 32

def main():
    temperatura = float(input('Digite a temperatura em graus Celsius: '))
    print(f'{temperatura}°C equivale a {convert_(temperatura):.2f}°F')         
    
if __name__ == '__main__':
    main()
    