"""
Testes da classe Produto.
"""
import unittest
import pytest
from datetime import datetime, timedelta

from produto import Produto


class TestProduto(unittest.TestCase):
    """Testa a classe Produto."""

    def setUp(self):
        self.produto = Produto(
            codigo="001",
            nome="Leite",
            preco=5.0,
            quantidade=20,
            data_validade=datetime.now() + timedelta(days=5),
            estoque_minimo=10
        )

    def test_inicializacao(self):
        self.assertEqual(self.produto.nome, "Leite")
        self.assertEqual(self.produto.preco, 5.0)
        self.assertEqual(self.produto.quantidade, 20)

    def test_adicionar_estoque(self):
        self.produto.adicionar_estoque(10)
        self.assertEqual(self.produto.quantidade, 30)

    def test_remover_estoque(self):
        sucesso = self.produto.remover_estoque(5)
        self.assertTrue(sucesso)
        self.assertEqual(self.produto.quantidade, 15)

        falha = self.produto.remover_estoque(100)
        self.assertFalse(falha)
        self.assertEqual(self.produto.quantidade, 15)

    def test_verificar_estoque_baixo(self):
        self.produto.quantidade = 5
        self.assertTrue(self.produto.verificar_estoque_baixo())

        self.produto.quantidade = 15
        self.assertFalse(self.produto.verificar_estoque_baixo())

    def test_calcular_valor_total(self):
        self.assertEqual(self.produto.calcular_valor_total(), 5.0 * 20)

    def test_verificar_validade(self):
        produto = Produto(
            codigo="002",
            nome="Arroz",
            preco=10.0,
            quantidade=30,
            data_validade=datetime.now() + timedelta(days=5),
            estoque_minimo=10
        )
        self.assertTrue(produto.verificar_validade())

        produto = Produto(
            codigo="003",
            nome="Feijão",
            preco=12.0,
            quantidade=25,
            data_validade=datetime.now() - timedelta(days=5),
            estoque_minimo=10
        )
        self.assertFalse(produto.verificar_validade())
        
    def test_remover_estoque_com_erro(self):
        produto = Produto("Feijão", 10, 10.0, 20)

        with self.assertRaises(ValueError):
            produto.remover_estoque(-10)

        self.assertTrue(produto.remover_estoque(10)) 

    def test_inicializacao_com_valores_padrao(self):
        produto = Produto(codigo="004", nome="Macarrão", preco=3.5)
        self.assertEqual(produto.quantidade, 0)  
        self.assertEqual(produto.estoque_minimo, 10)  
        self.assertIsNone(produto.data_validade)  

    def test_adicionar_estoque_com_quantidade_negativa(self):
        with self.assertRaises(ValueError):
            self.produto.adicionar_estoque(-5)

    def test_verificar_estoque_baixo_com_estoque_minimo(self):
        self.produto.quantidade = 10  
        self.assertFalse(self.produto.verificar_estoque_baixo())

    def test_remover_estoque_com_quantidade_igual(self):
        sucesso = self.produto.remover_estoque(20)
        self.assertTrue(sucesso)
        self.assertEqual(self.produto.quantidade, 0)

    def test_verificar_validade_sem_data(self):
        produto = Produto(
            codigo="005", nome="Feijão", preco=7.5, quantidade=15, estoque_minimo=5)
        self.assertTrue(produto.verificar_validade()) 

    def test_atualizar_quantidade_com_valor_negativo(self):
        with self.assertRaises(ValueError):
            self.produto.atualizar_quantidade(-10)

    def test_atualizar_quantidade(self):       
        self.produto.atualizar_quantidade(30)
        self.assertEqual(self.produto.quantidade, 30)

        with self.assertRaises(ValueError):
            self.produto.atualizar_quantidade(-5)

if __name__ == "__main__":
    unittest.main() 