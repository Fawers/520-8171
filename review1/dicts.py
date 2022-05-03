def nova_pessoa_tupla(nome, idade, dna):
    return (nome, idade, dna)


def nova_entidade_dict(nome, idade, rna):
    return {
        'nome': nome,
        'idade': idade,
        'rna': rna
    }


def main():
    ps = [
        nova_entidade_dict('Siiri', 25, 'ctug'),
    ]

    for p in ps:
        print(p['nome'], p['idade'], p['rna'])



if __name__ == '__main__':
    main()
