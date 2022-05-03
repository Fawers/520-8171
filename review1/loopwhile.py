def contagem(inicio):
    v = inicio

    while v > 0:
        print(v)
        v = v - 1

    print('zero')


def main():
    # não temos configurações
    contagem(8)


if __name__ == '__main__':
    main()
