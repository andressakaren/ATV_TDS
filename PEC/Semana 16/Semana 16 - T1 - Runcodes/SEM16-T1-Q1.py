# # 01.Faça um programa para ler uma matriz quadrada de ordem n e mostre uma tupla com a posição (linha e coluna) do
# maior e menor elemento. O valore de n é inteiro, positivo e deve ser informados pelo usuário.

def ler_matriz(n):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            valor = float(input())
            linha.append(valor)
            
        matriz.append(linha)
    return matriz

# fzr uma função p comparar 

def main():
    n = int(input())   
    matriz = ler_matriz(n)
    print(matriz)
    
if __name__ == "__main__":
    main()