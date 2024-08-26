def main():
    metrosAFrente = int(input())

    velTartaruga = 1 # m/min
    velLebre = 10 # m/min

    t = 0
    dist_tartaruga = metrosAFrente
    dist_lebre = 0 

    while dist_lebre < dist_tartaruga: 
        t += 1
        dist_tartaruga += velTartaruga   # ΔT = 1 min 
        dist_lebre += velLebre 

    print(t)

if __name__ == "__main__":
    main()