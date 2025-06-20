# Exercício - Revisão de estrutura de dados

# código (int)
# nome (str)
# categoria (str)
# preco (float)
# quantidade (int)

# Implemente um método na classe chamado valor_total(), que retorna o valor total em estoque do produto (preco × quantidade).

# Crie um dicionário chamado estoque, onde a chave é o código do produto (str) e o valor é um objeto Produto.

# Adicione pelo menos 4 produtos ao estoque com diferentes categorias e valores.

# Implemente as seguintes funcionalidades:

# a) Exibir todos os produtos no estoque com suas informações formatadas.

# b) Calcular e exibir o valor total geral do estoque.

# c) Exibir o nome do produto com o maior valor total.

# d) Permitir buscar produtos por categoria.

class Produto:
    def __init__(self, codigo, nome, categoria, preco, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.quantidade = quantidade

    def valor_total(self):
        return self.preco * self.quantidade


# estoque = Produto(101, 'Notebook', 'Eletronico', 2500, 40)
# print(estoque.nome)
# print(estoque.valor_total())

estoque = {}

estoque['101'] = Produto(101, 'Notebook', 'Eletrônicos', 2500.00, 5)
estoque['102'] = Produto(102, 'Cadeira Gamer', 'Móveis', 1200.00, 3)
estoque['103'] = Produto(103, 'Teclado Mecânico', 'Periféricos', 350.00, 10)
estoque['104'] = Produto(104, 'Celular', 'Eletrônicos', 1800.00, 7)


def exibir_todos_os_produtos():
    print()
    print('--- Produtos no Estoque ---')
    for produto in estoque.values():
        print(f'Código: {produto.codigo} | Nome: {produto.nome} | Categoria: {produto.categoria} | '
              f'Preço: R${produto.preco:.2f} | Quantidade: {produto.quantidade} | '
              f'Valor Total: R${produto.valor_total():.2f}')


def calcular_valor_total_geral():
    total = sum(produto.valor_total() for produto in estoque.values())
    print()
    print(f'Valor total geral do estoque: R${total:.2f}')


def exibir_produto_maior_valor():
    produto_maior_valor = None 
    maior_valor = 0

    for produto in estoque.values():
        valor_atual = produto.valor_total() 
        if valor_atual > maior_valor: 
            maior_valor = valor_atual  
            produto_maior_valor = produto 
            
    if produto_maior_valor: 
        print(
            f'\nProduto com maior valor total em estoque: {produto_maior_valor.nome} (R${produto_maior_valor.valor_total():.2f})')


def buscar_por_categoria():
    categoria_busca = input('\nDigite a categoria para buscar: ').capitalize()
    encontrados = []

    for produto in estoque.values():
        if produto.categoria == categoria_busca:
            encontrados.append(produto)

    if encontrados:
        print(f'\nProdutos na categoria "{categoria_busca}":')
        for p in encontrados:
            print(
                f'- {p.nome} (Preço: R${p.preco:.2f}, Quantidade: {p.quantidade})')
    else:
        print('Nenhum produto encontrado nessa categoria.')


def menu():
    while True:
        print('\n=== MENU ===')
        print('a) Exibir todos os produtos')
        print('b) Calcular valor total geral do estoque')
        print('c) Exibir o produto com maior valor total')
        print('d) Buscar produtos por categoria')
        print('s) Sair')
        opcao = input('Escolha uma opção: ').lower()

        if opcao == 'a':
            exibir_todos_os_produtos()
        elif opcao == 'b':
            calcular_valor_total_geral()
        elif opcao == 'c':
            exibir_produto_maior_valor()
        elif opcao == 'd':
            buscar_por_categoria()
        elif opcao == 's':
            print('Encerrando o programa...')
            break
        else:
            print('Opção inválida. Tente novamente.')


menu()
