def ops_lista():
    l = ['Mouse', 'Pen Tablet', 'Fone de ouvido', 'Saída VGA']

    l.append('Saída HDMI')
    l2 = l.copy()
    l.clear()
    l2.append('Mouse')
    print(l2.count('Mouse'))
    l.extend(l2)
    # l.append(l2)
    l.insert(0, 'Teclado')
    l.reverse()
    l.sort()
    l.sort(reverse=True)
    print(l.pop())
    print(l.pop(0))
    l.remove('Pen Tablet')
    print(l)


def referencias_de_listas():
    a = list(range(1, 6))
    b = a.copy()
    c = a

    print(f"A @ {id(a):x}")
    print(f"B @ {id(b):x}")
    print(f"C @ {id(c):x}")

    print("a is b", a is b)
    print("a is c", a is c)
    print("c is b", c is b)

    a.extend([6, 7])
    c.extend([8, 9])
    b.extend([10, 11])

    print('a', a)
    print('b', b)
    print('c', c)


def ops_dict():
    d = {
        'distancia': 80,  # em km
        'origem': 'são paulo',
        'destino': 'peruíbe'
    }

    d2 = d.copy()
    d.clear()

    print(d2['distancia'])
    print(d2.get('origem'))
    print(d2['destino'])
    print(d2.get('parada'))
    print(d2.get('parada obrigatória', 'graal'))

    d.update(d2)
    print(f"estou indo em direção a {d.pop('destino')}")
    print(f"e também sei que {d.popitem()}")
    d['total'] = 130
    print(d.setdefault('ideia', 51))
    print(d.setdefault('ideia', 120))

    for k in d.keys():
        print(k, end=', ')

    for v in d.values():
        print(v, end=', ')

    for (k, v) in d.items():
        print(k, v)


def de_para():
    dados = [('caneta', 'azul')]
    dados_dict = dict(dados)
    dados_list = list(dados_dict.items())

    print(dados)
    print(dados_dict)
    print(dados_list)

    print(dados == dados_list)
    print(dados is dados_list)


def main():
    # referencias_de_listas()
    # ops_lista()
    # ops_dict()
    de_para()


if __name__ == '__main__':
    main()
