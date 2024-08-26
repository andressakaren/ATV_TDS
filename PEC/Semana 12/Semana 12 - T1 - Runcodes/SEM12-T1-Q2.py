def main():
    precoAtual = float(input())

    valorPoupanca = 10000
    valorCarro = precoAtual

    mes = 0
    taxaPoupanca = 0.007
    taxaCarro = 0.004

    while valorPoupanca < valorCarro:
        mes += 1
        valorPoupanca += taxaPoupanca * valorPoupanca 
        valorCarro += taxaCarro * valorCarro
        
    print(mes)

if __name__ == "__main__":
    main()