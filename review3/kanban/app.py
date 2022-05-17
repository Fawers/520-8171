import kanban


def main():
    b = kanban.Board("Leituras", [])

    b.new_list("A fazer")
    b.new_list("Fazendo")
    b.new_list("Finalizados")

    b["A fazer"].add_card("Docker para Desenvolvedores")

    b.print_board()
    print('\n')

    b[0][0].move_right()
    b.print_board()
    print('\n')

    b[1][0].move_right()
    b.print_board()

if __name__ == '__main__':
    main()
