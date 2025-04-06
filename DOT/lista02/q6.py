# 6) Dadas duas listas, uma contendo a quantidade e a outra o preço de 20 produtos, elabore um programa que calcule e exiba o faturamento que é igual a quantidade x preço. Calcule e exiba também o faturamento total que é o somatório de todos os faturamentos, a média dos faturamentose quantos faturamentos estão abaixo da média.

def calcular_faturamentos(qntd, precos):
    faturamentos = []
    for i in range(len(qntd)):
        # quantidade x preço
        faturamentos.append(qntd[i] * precos[i])
    return faturamentos

def ler_lista(n, nome_lista):
    lista = []
    count = 0
    while count < n:
        try:
            valor = float(input(f"Digite o {count+1}° valor da lista de {nome_lista}: "))
            lista.append(valor)
            count += 1
        except ValueError:
            print("Valor inválido. Tente novamente.")
    return lista

quantidades = ler_lista(20, 'quantidades')
precos = ler_lista(20, 'preços')

faturamentos = calcular_faturamentos(quantidades, precos)
faturamento_total = sum(faturamentos)
media = faturamento_total / len(faturamentos)

abaixo_da_media = 0
for i in faturamentos:
    if i < media:
        abaixo_da_media += 1

print(f"Faturamento total: R${faturamento_total:.2f}")
print(f"Média de faturamento: R${media:.2f}")
print(f"Quantidade de faturamentos abaixo da média: {abaixo_da_media}")
