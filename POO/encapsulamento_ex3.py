# classe que calcula area de um retangulo com validações no acesso e na modificação dos atributos

class Retangulo:
    def __init__(self, largura, altura):
        self._largura = largura
        self._altura = altura

    # Propriedade de leitura para LARGURA
    @property
    def largura(self):
        return self._largura

    # Propriedade de escrita para largura
    @largura.setter
    def largura(self, valor):
        if valor > 0:
            self._largura = valor
        else:
            raise ValueError('A largura deve ser maior que zero!')

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        if valor > 0:
            self._altura = valor
        else:
            return ValueError('A altura deve ser maior que zero!')

    # Propriedade APENAS de leitura para área
    @property
    def area(self):
        return self._altura * self._largura
    
    def __str__(self):
        return f'Largura: {self._largura}\nAltura: {self._altura}\nÁrea: {self.area}'


# Criando um obj
ret = Retangulo(10, 5)

print(ret)
# Largura: 10
# Altura: 5
# Área: 50

# Acessando as propriedades como atributos 
print(ret.largura) # 10
print(ret.altura) # 5
print(ret.area) # 50

# refazer exemplo com atributos privados (encapsulamento_ex4.py)