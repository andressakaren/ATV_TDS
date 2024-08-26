def main():
    dataNascimento = input()
    i = 0
    numeroSorte = 0
    
    while i < len(dataNascimento): 
        numeroSorte += int(dataNascimento[i])
        i += 1
    print(numeroSorte)
    
if __name__ == '__main__':
    main()