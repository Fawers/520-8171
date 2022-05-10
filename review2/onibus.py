# - Crie uma classe que represente um ônibus. O ônibus deverá conter os seguintes atributos:
#   • capacidade total
#   • capacidade atual
#   • velocidade
#   • placa
# - Os comportamentos esperados para um Ônibus são:
#   • Acelerar
#   • Frear
#   • Embarcar
#   • Desembarcar
# Lembre-se que a capacidade total do ônibus é de 45 pessoas - não será possível admitir superlotação. Além disso, quando o ônibus ficar vazio, não será permitido efetuar o desembarque
# de pessoas.

class Onibus:
    def __init__(self, cap_total=45, cap_atual=0, velocidade=0, placa="XXX8171"):
        self.capacidade_total: int = cap_total
        self.capacidade_atual: int = cap_atual
        self.velocidade: int = velocidade
        self.placa: str = placa

    def acelerar(self, aceleracao: int):
        self.velocidade += aceleracao

        if self.velocidade < 0:
            self.velocidade = 0

    def frear(self, frenacao: int):
        self.acelerar(-frenacao)

    def embarcar(self, num_pessoas):
        if self.velocidade > 0:
            raise BusEmMovimento("Seu assassino!")

        nova_cap = self.capacidade_atual + num_pessoas

        if nova_cap > self.capacidade_total:
            self.capacidade_atual = self.capacidade_total
            raise Superlotacao(nova_cap - self.capacidade_total)

        self.capacidade_atual = nova_cap

    def desembarcar(self, num_pessoas):
        if self.velocidade > 0:
            raise BusEmMovimento("Seu assassino!")

        nova_cap = self.capacidade_atual - num_pessoas

        if nova_cap < 0:
            self.capacidade_atual = 0
            raise Vazio()

        self.capacidade_atual = nova_cap


class BusaoError(Exception):
    pass

class Superlotacao(BusaoError):
    pass

class Vazio(BusaoError):
    pass

class BusEmMovimento(BusaoError):
    pass


def main():
    bus = Onibus()
    # bus.desembarcar(45)
    bus.embarcar(10)
    bus.acelerar(80)
    print(bus.__dict__)
    bus.frear(40)
    print(bus.__dict__)
    # bus.embarcar(5)
    # bus.desembarcar(10)
    bus.frear(40)
    print(bus.__dict__)
    bus.desembarcar(10)
    bus.embarcar(40)
    print(bus.__dict__)

if __name__ == '__main__':
    main()
