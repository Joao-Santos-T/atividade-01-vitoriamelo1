"""
Módulo de análise financeira de pessoal.
"""
from dataclasses import dataclass


@dataclass
class Funcionario:
    """Modelo de funcionário utilizado para cálculos financeiros internos.

    Attributes:
        nome: Nome do funcionário
        matricula: Número de matrícula do funcionário
        salario_hora: Valor do salário por hora trabalhada
        horas_trabalhadas: Quantidade de horas trabalhadas no mês
        custo_empregador: Custo fixo mensal do empregador (INSS, FGTS, etc)
        tem_comissao: Indica se o funcionário recebe comissão
        valor_comissao: Valor da comissão por contrato fechado
        contratos_fechados: Número de contratos fechados no mês
    """

    nome: str
    matricula: int
    salario_hora: float = 100.0
    horas_trabalhadas: float = 0.0
    custo_empregador: float = 1000.0
    tem_comissao: bool = True
    valor_comissao: float = 100.0
    contratos_fechados: int = 0

    def obter_total_salario(self) -> float:
        if self.horas_trabalhadas < 0:
            raise ValueError("Quantidade de horas inválida.")
        return self.salario_hora * self.horas_trabalhadas

    def estimar_despesas(self) -> float:
        return self.obter_total_salario() + self.custo_empregador + self.obter_total_comissao()

    def obter_total_comissao(self) -> float:
        if not self.tem_comissao:
            return 0.0
        if self.contratos_fechados < 0:
            raise ValueError("Número de contratos inválido.")
        return self.valor_comissao * self.contratos_fechados