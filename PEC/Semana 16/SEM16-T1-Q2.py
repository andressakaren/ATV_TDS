def celcius_para_kelvin(temp_c):
    return round(temp_c + 273.15, 2)

def fahrenheit_para_kelvin(temp_f):
    return round(((temp_f - 32) * 5/9) + 273.15, 2)

def receber_temperatura():
    lista_temperaturas = []
    
    for i in range(12):
        temp = float(input())
        escala = str(input()).strip().upper()
        if escala == 'K':
            lista_temperaturas.append(round(temp, 2))
        elif escala == 'C':
            temp = celcius_para_kelvin(temp)
            lista_temperaturas.append(round(temp, 2))
        elif escala == 'F':
            temp = fahrenheit_para_kelvin(temp)
            lista_temperaturas.append(round(temp, 2))
        else:
            return receber_temperatura()

    return lista_temperaturas

def media_anual(temperatura):
    return round(sum(temperatura) / 12, 2)
    
def main():
    temperatura = receber_temperatura()
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho','Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro','Dezembro'] 
    media = media_anual(temperatura)
    
    print('TEMPERATURA MÉDIA ANUAL')
    print(f'{media}K')
    print('TEMPERATURAS ACIMA DA MÉDIA ANUAL:')
    
    for i in range(len(temperatura)):
        if temperatura[i] > media:
            print(f'{meses[i]}: {round(temperatura[i], 2)}K')
    
if __name__ == "__main__":
    main()