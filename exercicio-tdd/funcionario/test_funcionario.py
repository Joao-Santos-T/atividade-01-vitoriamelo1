"""
Testes da classe Funcionario com métodos renomeados.
"""
import unittest

from funcionario import Funcionario


class TestFuncionario(unittest.TestCase):
    """Testes da classe Funcionario."""

    def setUp(self):
        self.func = Funcionario(
            nome="João",
            matricula=123,
            salario_hora=50.0,
            horas_trabalhadas=160,
            custo_empregador=1000.0,
            tem_comissao=True,
            valor_comissao=200.0,
            contratos_fechados=5
        )

    def test_obter_total_salario(self):
        self.assertEqual(self.func.obter_total_salario(), 50.0 * 160)

    def test_estimar_despesas(self):
        salario = self.func.obter_total_salario()
        comissao = self.func.obter_total_comissao()
        custo_total_esperado = salario + self.func.custo_empregador + comissao
        self.assertEqual(self.func.estimar_despesas(), custo_total_esperado)

    def test_obter_total_comissao(self):
        self.assertEqual(self.func.obter_total_comissao(), 200.0 * 5)