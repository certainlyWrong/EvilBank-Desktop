from uuid import uuid4

from .log_model import LogModel
from .person_model import PersonModel
from ..controllers.log_controller import LogController


class AccountModel:

    __slots__ = [
        "__client",
        "__balance",
        "__limit",
        "__user",
        "__id",
        "__password",
    ]

    def __init__(
        self,
        client: PersonModel,
        user: str,
        password: str,
        balance: float,
        limit: float = 1000,
        id: str = str(uuid4()),
    ) -> None:
        self.__client = client
        self.__balance = balance
        self.__limit = limit
        self.__user = user
        self.__id = id
        self.__password = password

    def __withdraw(
        self,
        value: float,
        log: LogController | None = None,
    ) -> bool:
        """
        Realiza um saque na conta
        """
        request: bool = False

        if value > self.__balance:
            request = False
        else:
            self.__balance -= value
            request = True

        self.__newLog(
            log,
            "withdraw-Sucess" if request else "withdraw-Error",
            value
        )

        return request

    def __deposit(
        self,
        value: float,
        log: LogController | None = None,
    ) -> bool:
        """
        Realiza um deposito na conta
        """

        request = False

        if value > 0 and value <= self.__limit + self.__balance:
            self.__balance += value
            request = True

        self.__newLog(
            log,
            "deposit-Sucess" if request else "deposit-Error",
            value
        )

        return request

    def __transfer(
        self,
        value: float,
        destination: "AccountModel",
        log: LogController | None = None,
    ) -> bool:
        request = self.__withdraw(value) and destination.__deposit(value)

        self.__newLog(
            log,
            "transferSent-Sucess" if request else "transferSent-Error",
            value
        )

        destination.__newLog(
            log,
            "transferReceived-Sucess" if request else "transferReceived-Error",
            value
        )

        return request

    def __statement(
        self,
        log: LogController | None = None,
    ) -> None:
        """
        Imprime o extrato da conta
        """
        print(f"Saldo: {self.__balance}")

        self.__newLog(log, "statement", self.__balance)

    def __newLog(
        self,
        log: LogController | None = None,
        status: str = "new",
        value: float = 0,
    ) -> None:
        if log is not None:

            log.addLog(
                LogModel.create(
                    self.__id,
                    status,
                    str(value),
                )
            )

    def __str__(self) -> str:
        return (
            f"Name: {self.__client.firstName} {self.__client.lastName}\n"
            f"CPF: {self.__client.cpf}\n"
            f"Balance: {self.__balance}\n"
        )

    def __equals__(self, other: "AccountModel") -> bool:
        return (
            self.__client == other.__client
            and self.__balance == other.__balance
            and self.__limit == other.__limit
            and self.__user == other.__user
            and self.__id == other.__id
            and self.__password == other.__password
        )
