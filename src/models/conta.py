

from .cliente import Cliente
from ..controllers.historico import Historico


class Conta:
    def __init__(
        self,
        cliente: Cliente,
        saldo: float,
        limite: float = 1000
    ) -> None:
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()

    def sacar(self, valor: float) -> bool:
        request = False

        if valor > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor
            request = True

        self.historico.addLog(
            "Sacar-Sucesso:{}" if request else "Sacar-Falha:{}"
        )

        return request

    def depositar(self, valor: float) -> bool:
        request = False

        if valor > 0 and valor <= self.limite + self.saldo:
            self.saldo += valor
            request = True

        self.historico.addLog(
            "Deposito-Sucesso:{}" if request else "Deposito-Falha:{}"
        )
        return request

    def transfere(self, valor: float, destino: "Conta") -> bool:
        request = self.sacar(valor) and destino.depositar(valor)
        self.historico.addLog(
            "Transfe-Sucesso:{}" if request else "Transfe-Falha:{}"
        )
        return request

    def __equals__(self, other: "Conta") -> bool:
        return (
            self.cliente == other.cliente and
            self.saldo == other.saldo and
            self.limite == other.limite
        )

    def extrato(self) -> None:
        self.historico.addLog(
            "Extrato:{}"
        )

        print(f"Saldo: {self.saldo}")
