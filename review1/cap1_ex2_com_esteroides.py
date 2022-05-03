def substituir_caractere(s, *, busca, substituicao):
    if len(busca) > 1 or len(substituicao) > 1:
        return None

    return s.replace(busca, substituicao)

def select(*campos, from_, order_by='asc'):
    campos = ', '.join(campos)
    print(f"SELECT {campos} FROM {from_} ORDER BY {order_by}")

def main():
    # s = substituir_caractere(
    #     "minhaxgarrafaxestáxvazia", busca='x', substituicao=' ')
    # print(s)
    select("nome", "idade", "profissão", from_="pessoas", order_by='idade ASC')


if __name__ == '__main__':
    main()
