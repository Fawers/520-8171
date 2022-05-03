def meu_range(inicio, fim=None, passo=None):
    if fim is None:
        fim = inicio
        inicio = 0

    v = inicio

    if passo is None:
        passo = 1

    if passo > 0 and fim > inicio:
        while v < fim:
            print(v)
            v += passo

    elif passo < 0 and inicio > fim:
        while v > fim:
            print(v)
            v += passo


def contagem(inicio):
    for v in range(inicio, 0, -1):
        print(v)

    print('zero')


def main():
    # meu_range(10, 2, 2)
    contagem(6)


if __name__ == '__main__':
    main()
