def main():
    soma = " "
    ultimo = " "
    for i in range(10, 1001, 10):
        if i < 1000:
            i = str(i) + ',' + ' '
            soma += i
        else:
            i = str(i) + '.'
            ultimo += i
    print(f'Sequência: {soma.strip()} {ultimo.strip()}') 
        
if __name__ == "__main__":
    main()
        