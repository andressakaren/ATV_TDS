# classe que calcula area de um retangulo com validações no acesso e na modificação dos atributos

class Retangulo:
    def __init__(self, largura, altura):
        self.__largura = largura
        self.__altura = altura

    # Propriedade de leitura para LARGURA
    @property
    def largura(self):
        return self.__largura

    # Propriedade de escrita para largura
    @largura.setter
    def largura(self, valor):
        if valor > 0:
            self.__largura = valor
        else:
            raise ValueError('A largura deve ser maior que zero!')

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, valor):
        if valor > 0:
            self.__altura = valor
        else:
            raise ValueError('A altura deve ser maior que zero!')

    # Propriedade APENAS de leitura para área
    @property
    def area(self):
        return self.__altura * self.__largura

    def __str__(self):
        return f'Largura: {self.__largura}\nAltura: {self.__altura}\nÁrea: {self.area}'


# Criando um obj
ret = Retangulo(10, 5)

# print(ret)
# Largura: 10
# Altura: 5
# Área: 50

# Acessando as propriedades como atributos
# print(ret.largura) # 10
# print(ret.altura) # 5
# print(ret.area) # 50

# Modificando valores (validações inclusas)
ret.largura = 20
print(ret.area)  # 100

# tentar um valor inválido
try:
    ret.altura = -10  # Gera umm erro de atributo..
except ValueError as e:
    print(e)

# tentando acessar um atributo privado
try:
    print(ret.__largura)
except AttributeError as e:
    print('Erro ao tentar acessar o atributo:', e)
