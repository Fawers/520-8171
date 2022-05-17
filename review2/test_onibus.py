import unittest
import unittest.mock
# JUnit

from onibus import Onibus as O, Superlotacao, Vazio, BusEmMovimento


class TestOnibus(unittest.TestCase):
    def test_novo_onibus_possui_atributos_45_0_0(self):
        o = O()

        self.assertEqual(o.capacidade_total, 45)
        self.assertEqual(o.capacidade_atual, 0)
        self.assertEqual(o.velocidade, 0)

    def test_novo_onibus_possui_atributos_90_10_0(self):
        o = O(90, 10)

        self.assertEqual(o.capacidade_total, 90)
        self.assertEqual(o.capacidade_atual, 10)
        self.assertEqual(o.velocidade, 0)

    def test_acelerar_nao_zera_velocidade(self):
        o = O()

        self.assertEqual(o.velocidade, 0)
        o.acelerar(20)
        self.assertEqual(o.velocidade, 20)
        o.acelerar(20)
        self.assertEqual(o.velocidade, 40)

    def test_frear_zera_a_velocidade(self):
        o = O(velocidade=10)

        self.assertEqual(o.velocidade, 10)
        o.frear(7)
        self.assertEqual(o.velocidade, 3)
        o.frear(10)
        self.assertEqual(o.velocidade, 0)

    def test_embarcar_embarca_todos_os_passageiros(self):
        o = O()

        self.assertEqual(o.capacidade_atual, 0)
        o.embarcar(30)
        self.assertEqual(o.capacidade_atual, 30)

    def test_embarcar_explode_com_superlotacao_2(self):
        o = O()

        with self.assertRaises(Superlotacao) as sl:
            o.embarcar(47)

        self.assertEqual(sl.exception.args[0], 2)

    def test_embarcar_me_chama_de_assassino(self):
        o = O()

        o.acelerar(10)

        with self.assertRaises(BusEmMovimento) as bem:
            o.embarcar(1)

        self.assertIn("assassino", bem.exception.args[0])

    def test_desembarcar_explode_vazio(self):
        o = O()

        with self.assertRaises(Vazio):
            o.desembarcar(1)

