class Placa:
    CORES = {
        "fg_preto": "\x1b[30m",
        "fg_branco": "\x1b[37m",
        "bg_branco": "\x1b[47m",
        "bg_vermelho": "\x1b[41m",
    }

    def __init__(self, texto, cor_fonte, cor_fundo):
        self.texto = texto
        self.cor = cor_fonte
        self.cor_fundo = cor_fundo

    def __str__(self):
        fg = self.CORES["fg_" + self.cor]
        bg = self.CORES["bg_" + self.cor_fundo]
        return f"\x1b[1m{bg}{fg}{self.texto}\x1b[0m"


class PlacaLimiteVelocidade(Placa):
    def __init__(self, limite_velocidade: int):
        super().__init__(f"{limite_velocidade} km/h", "preto", "branco")


placa_pare = Placa("PARE", "branco", "vermelho")
placa_pe = Placa("∃", "preto", "branco")
placa_limite_50 = PlacaLimiteVelocidade(50)
placa_limite_120 = PlacaLimiteVelocidade(120)
placa_limite_30 = PlacaLimiteVelocidade(30)

print(placa_pare)
print(placa_pe)
print(placa_limite_50)
print(placa_limite_120)
