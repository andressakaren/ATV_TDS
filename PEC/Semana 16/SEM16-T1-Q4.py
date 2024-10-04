# A tabela abaixo demonstra a quantidade de vendas dos fabricantes de veículos durante o período de 2013 a 2018, em mil unidades.

# Fabricante / Ano	2013	2014	2015	2016	2017	2018
# Fiat	            204	    223	    230	    257	    290 	322
# Ford	            195 	192 	198 	203 	208 	228
# GM	            220 	222 	217 	231 	245 	280
# Wolkswagen	    254 	262 	270 	284 	296 	330

# Faça um programa em python que:

# leia os dados da tabela pelo teclado;
# leia um ano do período determine e exiba o fabricante que mais vendeu nesse ano;
# determine e exiba o ano de maior volume geral de vendas.
# determine e exiba a média anual de vendas de cada fabricante durante o período.

def valores_matriz(n=4, m=6): # seria os dados da tabela pra formar a matriz?
    matriz = []
    for i in range(n):
        linha = []
        for j in range(m):
            linha.append(int(input()))
        matriz.append(linha)
    return matriz

def maior_venda(ano, matriz):   
    anos = [2013, 2014, 2015, 2016, 2017, 2018]
    
    for i in range(len(anos)):
        if ano == anos[i]:
            maior = matriz[0][0]
            for j in range(len(matriz)):
                if matriz[j][i] > maior:
                    maior = matriz[j][i]
        return maior
    
def main():
    ano = int(input())
    matriz = valores_matriz()
    maiorVenda = maior_venda(ano, matriz)
    
    print(maiorVenda)
    
if __name__ == "__main__":
    main()