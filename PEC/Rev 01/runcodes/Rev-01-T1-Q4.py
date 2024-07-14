def main():
    tempoSeg = int(input(''))
    hh = tempoSeg // 3600
    mm = (tempoSeg % 3600) // 60
    ss = tempoSeg % 60
    print(f'{hh:02}:{mm:02}:{ss:02}')
if __name__ == '__main__':
    main()