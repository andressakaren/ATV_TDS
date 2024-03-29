def numero_inverso(num_digitado):
    d1 = num_digitado // 1000
    d2 = (num_digitado % 1000) // 100
    d3 = (num_digitado % 100) // 10
    d4 = (num_digitado % 10) // 1
    return d1, d2, d3, d4

numero = int(input())
dig1, dig2, dig3, dig4 = numero_inverso(numero)
print(f'{dig4}{dig3}{dig2}{dig1}')
