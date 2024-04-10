def soma_preco_morango(morango):
    return morango * (2.50 if morango <= 5 else 2.20)

def soma_preco_maca(maca):
    return maca * (1.80 if maca <= 5 else 1.50)

def comparacao(soma_kg, preco_total):
    if soma_kg > 8 or preco_total > 25: 
        return preco_total - (preco_total * 0.10)
    else:
        return preco_total
    
def main():
    morango = float(input('Digite a quantidade de morango, em kg: '))
    maca = float(input('Digite a quantidade de maca, em kg: '))
    soma_kg = morango + maca
    preco_total = soma_preco_morango(morango) + soma_preco_maca(maca)
           
    print(f'O valor total da compra é: R${comparacao(soma_kg, preco_total):.2f}')
    
if __name__ == '__main__':
    main()