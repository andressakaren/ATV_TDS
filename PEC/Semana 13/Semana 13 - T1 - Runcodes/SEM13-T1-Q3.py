def main():
    # a) preencha com valores reais lidos pelo teclado e imprima na ordem inversa. Considere até 4 (quatro) casas decimais.
    lista = []
    n = int(input())
    for i in range(n):
        num = float(input())
        num = round(num, 4)
        lista.insert(0, num)
    print(lista)
    
    # b) preencha com n notas lidas pelo teclado e imprima as notas e a média na tela. Considere 1 (uma) casa decimal. 
    lista = []
    if n == 0: 
        print(lista)
        print('SEM NOTAS')
    else:
        for i in range(n):
            num = float(input())
            num = round(num, 1)
            lista.append(num)
        print(lista)
        media = sum(lista)/n
        print(f'{media:.1f}')
    
    # c) preencha com n letras lidas pelo teclado e imprima quantas vogais foram lidas. Imprima as consoantes. 
    lista = []
    lista_consoante = []
    count = 0

    for i in range(n):
        letra = input().strip()
        lista.append(letra)
    
    for i in range(n):
        if lista[i] in 'aeiouAEIOU': 
            count += 1
        else:
            lista_consoante.append(lista[i])
    print(count)
    print(lista_consoante)
            
if __name__ == '__main__':
    main()