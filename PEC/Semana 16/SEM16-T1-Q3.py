def valores(n, m):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(m):
            valor = int(input())
            linha.append(valor)
        matriz.append(linha)
    return matriz

# a) a soma dos elementos da primeira linha ---- OK
def soma_primeiraLinha(matriz):
    return sum(matriz[0])

# b) a soma dos elementos da última coluna ---- OK
def soma_ultimaColuna(matriz):
    soma = 0
    for i in matriz: # i é linha, não um indice pq está iterando diretamente na matriz e nao no tamanho dela usando len.
        soma += i[-1]
    return soma

# c) a média de todos os elementos ---- OK
def media_todosElementos(matriz, n, m):
    soma = 0   
    for i in matriz:
        soma += sum(i)         
    return round(soma / (n * m), 4)

# d) o menor elemento ---- OK
def menor_Elemento(matriz):
    menor = matriz[0][0]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] < menor:
                menor = matriz[i][j]
    return menor

# e) o maior elemento ---- OK
def maior_Elemento(matriz):
    maior = matriz[0][0]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > maior:
                maior = matriz[i][j]
    return maior

def main():
    n = int(input())
    m = int(input())
    matriz = valores(n, m)
    
    somaPrimeiraLinha = soma_primeiraLinha(matriz)
    somaUltimaColuna = soma_ultimaColuna(matriz)
    mediaTodosElementos = media_todosElementos(matriz, n, m)
    menorElemento = menor_Elemento(matriz)
    maiorElemento = maior_Elemento(matriz)
    
    respostas = (somaPrimeiraLinha, somaUltimaColuna, mediaTodosElementos, menorElemento, maiorElemento)
    print(respostas)
        
if __name__ == "__main__":
    main()