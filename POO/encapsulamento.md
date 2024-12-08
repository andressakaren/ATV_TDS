# Encapsulamento - POO

## Definição

O encapsulamento é um dos pilares da Programação Orientada a Objetos (POO). Ele se refere à ideia de **ocultar os detalhes internos de uma classe** e expor apenas o que é necessário por meio de métodos públicos (interface). Isso ajuda a proteger os dados e a organizar melhor o código.

No Python, o encapsulamento é implementado usando convenções de nomenclatura para os atributos e métodos de uma classe:

### 1. **Atributos Públicos**

- Podem ser acessados diretamente fora da classe.
- Geralmente, são usados quando não há necessidade de proteger o dado.

### 2. **Atributos Protegidos**

- Usam um **underscore (`_`) antes do nome**.
- Indicam que **não devem ser acessados diretamente**, mas isso não impede o acesso.
- É apenas uma **convenção**.

### 3. **Atributos Privados**

- Usam **dois underscores (`__`) antes do nome**.
- São **"escondidos"** da interface pública da classe.
- Só podem ser acessados indiretamente, geralmente por métodos públicos.

---

### Exemplo Simples de Encapsulamento

Imagine uma classe que representa uma conta bancária:

```python
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular  # Atributo público
        self._saldo = saldo     # Atributo protegido

    # Método público para acessar o saldo
    def mostrar_saldo(self):
        return f"Saldo atual: R${self._saldo:.2f}"

    # Método público para alterar o saldo
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
        else:
            print("O valor do depósito deve ser positivo!")

    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
        else:
            print("Saldo insuficiente ou valor inválido!")

# Uso da classe
conta = ContaBancaria("Andressa", 500.0)

# Acessando métodos públicos
print(conta.mostrar_saldo())  # Saldo atual: R$500.00

conta.depositar(100)          # Depósito de R$100
print(conta.mostrar_saldo())  # Saldo atual: R$600.00

conta.sacar(200)              # Saque de R$200
print(conta.mostrar_saldo())  # Saldo atual: R$400.00
```

---

### Exemplo com Atributos Privados

```python
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular      # Atributo público
        self.__saldo = saldo        # Atributo privado

    def mostrar_saldo(self):
        return f"Saldo atual: R${self.__saldo:.2f}"

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("O valor do depósito deve ser positivo!")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente ou valor inválido!")

# Uso da classe
conta = ContaBancaria("Andressa", 500.0)

print(conta.mostrar_saldo())  # Saldo atual: R$500.00

# Não é possível acessar diretamente __saldo
# print(conta.__saldo)        # AttributeError
```

---

### Benefícios do Encapsulamento

1. **Segurança dos Dados**: Previne que atributos sejam alterados diretamente de forma errada.
2. **Facilidade de Manutenção**: Permite alterar a implementação interna sem impactar o restante do código.
3. **Controle**: Oferece controle sobre como os dados podem ser acessados ou modificados.

---

## `@property` e `@<nome>.setter`

O `@property` e o `@<nome>.setter` são **decoradores** em Python que facilitam o uso de **propriedades** em classes. Eles permitem que você trate métodos como se fossem atributos, promovendo um estilo de código mais limpo e intuitivo.

---

### **O que é `@property`?**

O `@property` transforma um método em uma **propriedade de leitura**. Isso significa que você pode acessar o retorno do método como se fosse um atributo, sem precisar chamar explicitamente o método com parênteses.

### **O que é `@<nome>.setter`?**

O `@<nome>.setter` é usado para criar uma **propriedade de escrita**. Ele permite que você defina um método que será chamado quando tentar **atribuir um valor** a essa propriedade.

---

### **Por que usar `@property` e `@setter`?**

Eles são úteis para:

1. **Proteger o acesso a atributos internos**.
2. Adicionar **validações** ao acessar ou modificar os valores de atributos.
3. Facilitar futuras alterações no comportamento interno da classe, sem impactar o código que usa a classe.

---

### **Exemplo Prático: Classe de Retângulo**

Vamos criar uma classe que calcula a área de um retângulo com validações no acesso e na modificação dos atributos.

```python
class Retangulo:
    def __init__(self, largura, altura):
        self._largura = largura
        self._altura = altura

    # Propriedade de leitura para largura
    @property
    def largura(self):
        return self._largura

    # Propriedade de escrita para largura
    @largura.setter
    def largura(self, valor):
        if valor > 0:
            self._largura = valor
        else:
            raise ValueError("A largura deve ser maior que zero!")

    # Propriedade de leitura para altura
    @property
    def altura(self):
        return self._altura

    # Propriedade de escrita para altura
    @altura.setter
    def altura(self, valor):
        if valor > 0:
            self._altura = valor
        else:
            raise ValueError("A altura deve ser maior que zero!")

    # Propriedade apenas de leitura para área
    @property
    def area(self):
        return self._largura * self._altura


# Uso da classe
ret = Retangulo(10, 5)

# Acessando as propriedades como atributos
print(ret.largura)  # 10
print(ret.altura)   # 5
print(ret.area)     # 50

# Modificando valores (validações inclusas)
ret.largura = 20
print(ret.area)     # 100

# Tentar um valor inválido
try:
    ret.altura = -10  # Gera um erro
except ValueError as e:
    print(e)  # "A altura deve ser maior que zero!"
```

---

### **Vantagens do Uso de `@property`**

1. **Interface uniforme**: O código que usa a classe não precisa mudar se você decidir implementar validações ou lógica adicional para um atributo.
2. **Controle**: Permite proteger e controlar o acesso aos dados.
3. **Código limpo**: O acesso e a alteração dos atributos parecem simples, como se fossem atributos comuns.

---

### Diferença entre `@property` e `@<nome>.setter`

| Aspecto              | `@property`                   | `@<nome>.setter`            |
|-----------------------|-------------------------------|-----------------------------|
| Propósito            | Criar uma propriedade de leitura (get). | Criar uma propriedade de escrita (set). |
| Uso                  | Usado para acessar valores.     | Usado para modificar valores. |
| Exemplo de sintaxe    | `@property\ndef atributo(self): ...` | `@atributo.setter\ndef atributo(self, valor): ...` |
