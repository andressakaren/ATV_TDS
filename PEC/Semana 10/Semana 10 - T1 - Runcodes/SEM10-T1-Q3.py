def main():
    soma = 0
        
    for i in range(100):
        i = int(input())
        soma += i
        
    media = soma / 100
    print(f'{media:.2f}')
        
if __name__ == "__main__":
    main()