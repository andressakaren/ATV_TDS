def media_semestral(n1, n2):
    media = (n1 + n2) / 2
    return round(media, 2)

def main():
    assert media_semestral(10, 8) == 9.0
    assert media_semestral(5.5, 6.5) == 6.0
    assert media_semestral(0, 0) == 0.0
    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()
