# INCOMPLETA

def ler_nomes(n):
    lista_nomes = []
    for i in range(n):
        nome = input().strip()
        lista_nomes.append(nome)
    return lista_nomes

def ler_alturas(n):
    lista_alturas = []
    for i in range(n):
        altura = input()
        lista_alturas.append(altura)
    return lista_alturas

def media_altura(lista):
    media = sum(lista)/len(lista)
    return media 

def main():
    qtdJogadores = 12
    lista_nomes = ler_nomes(qtdJogadores)
    lista_alturas = ler_alturas(qtdJogadores)
    media = media_altura(lista_alturas)
    
    maiorAltura = max(lista_alturas)
    index_maiorAltura = lista_alturas.index(maiorAltura)
    nomeMaisAlto = lista_nomes[index_maiorAltura]

    print('JOGADOR MAIS ALTO DO TIME')
    print(nomeMaisAlto) # nome 
    print(f'{maiorAltura:.2f}') # maior altura

    print('ALTURA MÉDIA DO TIME')
    print(f'{media:.2f}')    

    print('JOGADORES MAIS ALTOS QUE A MÉDIA DO TIME')
    for i in range(qtdJogadores):
        if lista_alturas[i] >= media:           
            print(lista_nomes[i])
            print(f'{lista_alturas[i]:.2f}')

    
if __name__ == '__main__':
    main()