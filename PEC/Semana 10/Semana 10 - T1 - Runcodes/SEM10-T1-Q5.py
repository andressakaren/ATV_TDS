def main():
    maior = 0
    
    for i in range(100):
        i = int(input())
        if i > maior:
            maior = i
    print(f'{maior}')
    
if __name__ == "__main__":
    main()