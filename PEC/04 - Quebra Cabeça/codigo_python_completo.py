# separar.png
# Responsável por separar as data inserida no formato DDMMAAAA e colocar em variáveis correspondentes ao seu significado 

# A função "separar_data" recebe o parâmetro "dma"
def separar_data(dma):
    # A variável "a" recebe o resultado da equação
    a = dma % 10000
    # A variável "dma" recebe a parte inteira da divisão
    dma //= 10000
    
    # A variável "m" recebe o resultado da equação
    m = dma % 100
    # A variável "dma" recebe a parte inteira da divisão
    dma //= 100
    
    # A variável "b" recebe o resultado da variável
    d = dma
    # Retorna as variáveis "d", "m", "a"
    return d, m, a


# signo.png
# Responsável por procurar os signos levando em consideração os parâmetros "dia" e "mes"

# A função "signo" recebe o parâmetro "dia" e "mes"
def signo(dia, mes):
    # Condição para o valor do parâmetro "mes"
    if mes == 3:
        return 'Peixes' if dia < 21 else 'Áries'
    # Condição para o valor do parâmetro "mes"
    if mes == 4:
        return 'Áries' if dia < 20 else 'Touro'
    # Condição para o valor do parâmetro "mes"
    if mes == 5:
        return 'Touro' if dia < 21 else 'Gêmeos'
    # Condição para o valor do parâmetro "mes"
    if mes == 6:
        return 'Gêmeos' if dia < 22 else 'Câncer'
    # Condição para o valor do parâmetro "mes"
    if mes == 7:
        return 'Câncer' if dia < 23 else 'Leão'
    # Condição para o valor do parâmetro "mes"
    if mes == 8:
        return 'Leão' if dia < 23 else 'Virgem'
    # Condição para o valor do parâmetro "mes"
    if mes == 9:
        return 'Virgem' if dia < 23 else 'Libra'
    # Condição para o valor do parâmetro "mes"
    if mes == 10:
        return 'Libra' if dia < 23 else 'Escorpião'
    # Condição para o valor do parâmetro "mes"
    if mes == 11:
        return 'Escorpião' if dia < 22 else 'Sagitário'
    # Condição para o valor do parâmetro "mes"
    if mes == 12:
        return 'Sagitário' if dia < 22 else 'Capricórnio'
    # Condição para o valor do parâmetro "mes"
    if mes == 1:
        return 'Capricórnio' if dia < 20 else 'Aquário'
    # Condição para o valor do parâmetro "mes"
    if mes == 2:
        return 'Aquário' if dia < 19 else 'Peixes'

# remover.png
# importa a função para transformar string (padrão unicode) em forma normal (representação binária)  

# A função "remover_acentos" recebe o parâmetro "texto"
def remover_acentos(texto):
    # Importa "normalize" da biblioteca "unicodedata"
    from unicodedata import normalize
    return normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')

# horoscopo
# importa a função para abrir e ler URLs; E retorna a frase retirada da url definida 

# A função "horoscopo" recebe o parâmetro "signo_desejado"
def horoscopo(signo_desejado):
    # Importa "normalize" da biblioteca "unicodedata"
    import urllib.request
    
    # A variável "signo_formatado" recebe a chamada de função já transformada para minúscula    
    signo_formatado = remover_acentos(signo_desejado).lower()
    
    # A variável "minha_url" recebe o link e o signo já formatado
    minha_url = 'https://www.horoscopovirtual.com.br/horoscopo/' + signo_formatado
    
    # Chama o módulo urllib.request 
    requisicao = urllib.request.Request(
        url= minha_url,
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    resposta = urllib.request.urlopen(requisicao)
    pagina = resposta.read().decode('utf-8')
    marcador_inicio = '<p class="text-pred">'
    marcador_final = '</p>'

    inicio = pagina.find(marcador_inicio) + len(marcador_inicio) 
    final = pagina.find(marcador_final, inicio)
    
    return signo_desejado + ': ' + pagina[inicio:final]

# main.png
# Bloco principal, onde são inseridos as informações pelo teclado e mostrado para o usuário

# Declara uma função principal
def main():
    # Entrada de dados
    nascimento = int(input('Digite sua data de nascimento no formato DDMMAAAA: '))
    # Processamento
    dia, mes, _ = separar_data(nascimento)
    meu_signo = signo(dia, mes)
    horoscopo_de_hoje = horoscopo(meu_signo)
    # Saída de dados
    print(horoscopo_de_hoje)
    
# name.png
# Condição para executar uma parte específica do código em outro arquivo
if __name__ == '__main__':
    main()