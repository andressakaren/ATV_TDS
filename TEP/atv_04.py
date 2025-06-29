import numpy as np

print("\n1. CRIAÇÃO DO DATASET")
print("-" * 30)

# Gerar dados aleatórios
np.random.seed(42)
ids = np.arange(1, 11) 
precos = np.random.randint(20, 200, size=10) 
vendas_a = np.random.randint(50, 500, size=10) 
vendas_b = np.random.randint(30, 400, size=10) 
custos = np.random.randint(10, 150, size=10) 

dataset = np.column_stack((ids, precos, vendas_a, vendas_b, custos))

# Exibir o dataset com cabeçalhos para melhor visualização
colunas = ['ID', 'Preço', 'Vendas_A', 'Vendas_B', 'Custo']
print(f"{'ID':<4} {'Preço':<8} {'Vendas_A':<10} {'Vendas_B':<10} {'Custo':<8}")
print("-" * 45)
for i, linha in enumerate(dataset):
    print(f"{int(linha[0]):<4} R${linha[1]:<7.0f} {int(linha[2]):<10} {int(linha[3]):<10} R${linha[4]:<7.0f}")

print("\n\n2. DADOS")
print("-" * 30)

print(f"Formato do array: {dataset.shape}")
print(f"Tipo dos dados: {dataset.dtype}")
print(f"Número total de elementos: {dataset.size}")

print("\nValores mínimos por coluna:")
for i, col in enumerate(colunas):
    print(f"{col}: {dataset[:, i].min()}")

print("\nValores máximos por coluna:")
for i, col in enumerate(colunas):
    print(f"{col}: {dataset[:, i].max()}")

print("\n\n3. CÁLCULOS ESTATÍSTICOS")
print("-" * 30)


print("ESTATÍSTICAS DAS VENDAS:")
print(f"Região A - Média: {vendas_a.mean():.2f}, Mediana: {np.median(vendas_a):.2f}, Desvio Padrão: {vendas_a.std():.2f}")
print(f"Região B - Média: {vendas_b.mean():.2f}, Mediana: {np.median(vendas_b):.2f}, Desvio Padrão: {vendas_b.std():.2f}")

receita_a = precos * vendas_a
receita_b = precos * vendas_b

print(f"\nRECEITA TOTAL POR REGIÃO:")
print(f"Região A: R$ {receita_a.sum():,.2f}")
print(f"Região B: R$ {receita_b.sum():,.2f}")


margem_lucro = precos - custos
produto_maior_margem = np.argmax(margem_lucro)

print(f"\nMARGEM DE LUCRO:")
print(f"Produto com maior margem: ID {int(ids[produto_maior_margem])}")
print(f"Margem de lucro: R$ {margem_lucro[produto_maior_margem]:.2f}")

print("\nMargem de lucro por produto:")
for i in range(len(ids)):
    print(f"ID {int(ids[i])}: R$ {margem_lucro[i]:.2f}")

print("\n\n4. MANIPULAÇÃO DE DADOS")
print("-" * 30)

# Adicionar coluna de Receita Total
receita_total = receita_a + receita_b
dataset_expandido = np.column_stack((dataset, receita_total))

print("Dataset com Receita Total:")
print(f"{'ID':<4} {'Preço':<8} {'Vendas_A':<10} {'Vendas_B':<10} {'Custo':<8} {'Rec_Total':<12}")
print("-" * 58)
for linha in dataset_expandido:
    print(f"{int(linha[0]):<4} R${linha[1]:<7.0f} {int(linha[2]):<10} {int(linha[3]):<10} R${linha[4]:<7.0f} R${linha[5]:<11,.2f}")

# Filtrar produtos com receita total acima de R$10.000
filtro_alta_receita = receita_total > 10000
produtos_alta_receita = dataset_expandido[filtro_alta_receita]

print(f"\nProdutos com receita total acima de R$ 10.000:")
if len(produtos_alta_receita) > 0:
    print(f"{'ID':<4} {'Preço':<8} {'Vendas_A':<10} {'Vendas_B':<10} {'Custo':<8} {'Rec_Total':<12}")
    print("-" * 58)
    for linha in produtos_alta_receita:
        print(f"{int(linha[0]):<4} R${linha[1]:<7.0f} {int(linha[2]):<10} {int(linha[3]):<10} R${linha[4]:<7.0f} R${linha[5]:<11,.2f}")
else:
    print("Nenhum produto com receita acima de R$ 10.000")