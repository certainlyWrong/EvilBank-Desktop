from datetime import datetime


class Historico:
    def __init__(self) -> None:
        self._data_abertura = datetime.now()
        self._transacoes: list[str] = []

    def view(self):
        print(f"Data de abertuda: {self._data_abertura}")
        print("Transações:")

        for t in self._transacoes:
            print(f"\t- {t}")

    def addLog(self, log: str):
        self._transacoes.append(log.format(datetime.now()))
