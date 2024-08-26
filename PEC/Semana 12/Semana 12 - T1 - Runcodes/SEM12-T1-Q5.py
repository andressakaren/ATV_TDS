def main():
    populacaoInicial = int(input())
    populacaoAtual = populacaoInicial
    ano = 1599
    
    # O programa encerra sua execução quanto a população total cai para menos de 10% da população original.
    # populacaoAtual < 0.1 * populacaoInicial (FALSE)
    # populacaoAtual >= 0.1 * populacaoInicial (TRUE)

    while populacaoAtual >= 0.1 * populacaoInicial:
        nascimento = 0.01 * populacaoAtual
        mortes = 0.06 * populacaoAtual
        
        populacaoAtual = populacaoAtual + nascimento - mortes
        ano += 1
        
        print(f'{ano},{nascimento:.0f},{mortes:.0f},{populacaoAtual:.0f}')

if __name__ == '__main__':
    main()