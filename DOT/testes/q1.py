# 1) Escreva uma função que recebe uma lista com n números inteiros, retornar uma lista eliminando as repetições. Ex: [5, 4, 5, 7, 3, 4] = [5, 4, 7, 3]

def eliminar_repeticoes(lista):
    if not isinstance(lista, list):
        return Exception
    resultado = []
    for numero in lista:
        if numero not in resultado:
            resultado.append(numero)
    return resultado

entrada = [5, 4, 5, 7, 3, 4]
saida = eliminar_repeticoes(entrada)
print(saida) 


assert eliminar_repeticoes([5, 4, 5, 7, 3, 4]) == [5, 4, 7, 3]
# assert eliminar_repeticoes([]) == []
assert eliminar_repeticoes([1, 1, 1, 1]) == [1]
assert eliminar_repeticoes([1, 2, 3, 4]) == [1, 2, 3, 4]
assert eliminar_repeticoes('123') == Exception
assert eliminar_repeticoes(None) == Exception
print('Todos os testes OK')


# assert eliminar_repeticoes()


# assert eliminar_repeticoes("123") == Exception
# assert eliminar_repeticoes(123) == Exception
# assert eliminar_repeticoes(None) == Exception