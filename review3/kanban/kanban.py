from itertools import zip_longest
from datetime import datetime
from dataclasses import dataclass

import exceptions as e


@dataclass
class Card:
    name: str
    description: str
    start_date: datetime | None
    due_date: datetime | None
    list: 'List'

    def move_right(self):
        l = self.list
        b = l.board

        i = b.lists.index(l)

        try:
            l2 = b[i+1]

        except e.ListNotFound:
            pass

        else:
            l.cards.remove(self)
            l2.cards.append(self)
            self.list = l2


class List:
    def __init__(self, name: str, board: 'Board', cards: list[Card]):
        self.name = name
        self.board = board
        self.cards = cards

    def __getitem__(self, index_or_name: str | int) -> Card:
        match index_or_name:
            case str():
                for c in self.cards:
                    if c.name == index_or_name:
                        return c

            case int():
                try:
                    return self.cards[index_or_name]

                except IndexError:
                    pass

        raise e.CardNotFound(index_or_name)

    def __str__(self):
        return f"List({self.name!r})"

    def add_card(self, card_name: str) -> Card:
        c = Card(card_name, '', None, None, self)
        self.cards.append(c)
        return c


class Board:
    def __init__(self, name: str, lists: list[List]):
        self.name = name
        self.lists = lists

    def __getitem__(self, index_or_name: str | int) -> List:
        if isinstance(index_or_name, str):
            for l in self.lists:
                if l.name == index_or_name:
                    return l

        else:
            try:
                return self.lists[index_or_name]

            except IndexError:
                pass

        raise e.ListNotFound(index_or_name)

    def __str__(self):
        return f"Board({self.name!r})"

    def new_list(self, name: str) -> List:
        self.lists.append(l := List(name, self, []))
        return l

    def print_board(self):
        print(f"{self.name:-^90}\n")

        for l in self.lists:
            print(f"{l.name:=^29}", end='|')

        print()

        # zip(*[[cards da lista 0], [cards da lista 1], [cards da lista 2]])
        # zip([cards da lista 0], [cards da lista 1], [cards da lista 2])
        # [(cl1, cl2, cl3), (cl1, cl2, cl3), ...]

        for cards in zip_longest(*[l.cards for l in self.lists]):
            for c in cards:
                if c is not None:
                    print(f"{c.name:^29}", end='|')

                else:
                    print(f"{'':^29}", end='|')
            print()
