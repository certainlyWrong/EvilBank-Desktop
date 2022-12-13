

from src.models.cliente import Cliente
from src.models.conta import Conta


if __name__ == '__main__':
    # Teste a classe conta

    cliente1 = Cliente('João', 'sousa', '123.456.789-10')
    cliente2 = Cliente('Maria', 'sousa', '123.456.789-10')

    conta1 = Conta(cliente1, 1000, 1000)
    conta2 = Conta(cliente2, 1000, 1000)

    conta1.depositar(100)
    conta1.sacar(100)
    conta1.transfere(100, conta2)

    conta1.extrato()
    conta2.extrato()
