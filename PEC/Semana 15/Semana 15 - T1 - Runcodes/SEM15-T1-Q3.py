def carrega_cidades():
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            resultado.append(
                (uf, int(ibge), nome, int(dia), int(mes), int(pop))
            )
    arquivo.close()
    return resultado

# print(cidades[:3] + cidades[-2:])

def aniversario_cidades(dia, mes, cidades):
    lista_cidades_aniversario = []
    # ARRUMAR ALGUMA FORMA DE IMPRIMIR DE FORMA INDIVIDUAL EM OUTRA LINHA
    for cidade in cidades:
        if cidade[3] == dia and cidade[4] == mes:
            lista_cidades_aniversario.append(cidade[2])
    return lista_cidades_aniversario

def main():
    cidades = carrega_cidades() # tem a lista de todas as cidades com as informações
    
    dia = int(input())
    mes = int(input())
    
    print(aniversario_cidades(dia, mes, cidades))

if __name__ == "__main__":
    main()

