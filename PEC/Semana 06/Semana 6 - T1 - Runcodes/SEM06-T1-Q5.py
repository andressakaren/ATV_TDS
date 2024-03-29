def pagamento_avista (valor_compra):
    return valor_compra - (valor_compra * (9/100))

def pagamento_5vezes (valor_compra):
    return valor_compra / 5

def pagamento_10vezes(valor_compra):
    return (valor_compra + (valor_compra * (17/100))) / 10

def main():
    valor_compra = float(input())
    
    print(f'{pagamento_avista(valor_compra):.2f}')
    print(f'{pagamento_5vezes(valor_compra):.2f}')
    print(f'{pagamento_10vezes(valor_compra):.2f}')

if __name__ == '__main__':
    main()
    