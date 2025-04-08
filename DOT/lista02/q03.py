# 3) Faça um programa que dada uma seqüência de n números, imprimi-la na ordem inversa à da leitura.

def ler_sequencia(n):
    count = 0
    lista_original = []
    while count < n:
        try: 
            num = float(input(f'Digite o {count+1}° número: '))
            lista_original.append(num)
            count += 1
        except:
            print('Digite um número válido')
            
    return lista_original

lista = ler_sequencia(5)
lista_invertida = lista[::-1]
print('Lista original:', lista)  
print('Lista invertida:', lista_invertida)  