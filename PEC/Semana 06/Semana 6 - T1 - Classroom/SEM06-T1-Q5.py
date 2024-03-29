def pagamento_avista (valor_compra):
    return valor_compra - (valor_compra * (9/100))

def pagamento_5vezes (valor_compra):
    return valor_compra / 5

def pagamento_10vezes(valor_compra):
    return (valor_compra + (valor_compra * (17/100))) / 10

def main():
    valor_compra = float(input('Digite o valor do preço do produto: R$'))
    
    print(f'Valor para pagamento à vista, com desconto de 9%: R${pagamento_avista(valor_compra):.2f}.')
    print(f'Valor da prestação para pagamento em 5 vezes, sem desconto nem juros: R${pagamento_5vezes(valor_compra):.2f}.')
    print(f'Valor da prestação para pagamento em 10 vezes, com 17% de juros: R${pagamento_10vezes(valor_compra):.2f}.')

if __name__ == '__main__':
    main()
    