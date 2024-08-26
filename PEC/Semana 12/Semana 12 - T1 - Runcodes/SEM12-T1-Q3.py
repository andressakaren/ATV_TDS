def main():
    pais_X = int(input())
    pais_Y = int(input())
    
    ano = 0
    taxaA = 0.02
    taxaB = 0.03

    if pais_X > pais_Y:
        pais_A = pais_X
        pais_B = pais_Y
    else:
        pais_A = pais_Y
        pais_B = pais_X
    
    populacao_variavel_A = pais_A
    populacao_variavel_B = pais_B
   
    while populacao_variavel_A > populacao_variavel_B:
        ano += 1
        populacao_variavel_A += taxaA * populacao_variavel_A
        populacao_variavel_B += taxaB * populacao_variavel_B
    
    print(ano)
    
if __name__ == '__main__':
    main()