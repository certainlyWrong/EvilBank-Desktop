import json
import sqlite3
from rich import print

from ..models.account_model import AccountModel
from .log_controller import LogController


class BankController:
    __slots__ = [
        "__name",
        "__agency",
        "__sqlite",
        "__querys",
        "__accounts",
        "__balance",
        "log",
    ]

    def __init__(
        self,
        name: str,
        agency: str,
        balance: float,
    ):
        self.__name = name
        self.__agency = agency
        self.__sqlite = sqlite3.connect("resources/bank.db")
        self.__querys = self.loadQuerys()

        self.__accounts = {}
        self.__balance = balance
        self.log = LogController("resources/bank.db")

    def loadQuerys(self) -> dict:
        with open("resources/querys/bank_querys.json", "r") as file:
            return json.load(file)

    def createAccountsTable(self) -> None:
        self.__sqlite.execute(self.__querys["createAccountsTable"])
        self.__sqlite.commit()

    def addAccount(self, account: AccountModel) -> None:
        self.__accounts[account.__user] = account

    def removeAccount(self, account: AccountModel) -> AccountModel | None:
        return self.__accounts.pop(account.__user)

    def accountByLogin(self, user: str, password: str) -> AccountModel | None:
        result = None

        account = self.__accounts.get(user)
        if account is not None:
            if account.password == password:
                result = account
        return result

    def accountByCPF(self, cpf: str) -> AccountModel | None:
        result = None

        for account in self.__accounts.values():
            if account.cliente.cpf == cpf:
                result = account

        return result

    def accountByUserName(self, name: str) -> AccountModel | None:
        result = None

        for account in self.__accounts.values():
            if account.cliente.nome == name:
                result = account

        return result

    def viewAccount(self, user: str, password: str) -> None:
        account = self.accountByLogin(user, password)
        if account is not None:
            print(account)

    def viewAllAccounts(self) -> None:
        for account in self.__accounts.values():
            print(account)

    def withdrawByUserAndPassword(
        self,
        user: str,
        password: str,
        value: float,
    ) -> bool:
        """
        Realiza um saque na conta
        """

        result = False
        account = self.accountByLogin(user, password)
        if account is not None:
            result = account.__withdraw(value, self.log)
        return result

    def withdrawByAccount(self, account: AccountModel, value: float) -> bool:
        """
        Realiza um saque na conta
        """

        result = False
        if account is not None:
            result = account.__withdraw(value, self.log)
        return result

    def depositByUserAndPassword(
        self,
        user: str,
        password: str,
        value: float,
    ) -> bool:
        """
        Realiza um deposito na conta
        """

        result: bool = False
        account = self.accountByLogin(user, password)
        if account is not None:
            result = account.__deposit(value, self.log)
        return result

    def depositByAccount(self, account: AccountModel, value: float) -> bool:
        """
        Realiza um deposito na conta
        """

        result: bool = False
        if account is not None:
            result = account.__deposit(value, self.log)
        return result

    def transferByDestinationCPF(
        self,
        user: str,
        password: str,
        value: float,
        cpf: str,
    ) -> bool:
        """
        Realiza uma transferencia para uma conta destino
        a partir do CPF
        """
        result: bool = False
        account = self.accountByLogin(user, password)
        if account is not None:
            destination = self.accountByCPF(cpf)
            if destination is not None:
                result = account.__withdraw(value)
                if result:
                    result = destination.__deposit(value)
        return result

    def transferByDestinationUserName(
        self,
        user: str,
        password: str,
        value: float,
        userName: str,
    ) -> bool:
        """
        Realiza uma transferencia para uma conta destino
        a partir do nome de usuario
        """
        result: bool = False
        account = self.accountByLogin(user, password)
        if account is not None:
            destination = self.accountByUserName(userName)
            if destination is not None:
                result = account.__transfer(value, destination)
        return result

    def transferByAccounts(
        self,
        account: AccountModel,
        value: float,
        destination: AccountModel,
    ) -> bool:
        """
        Realiza uma transferencia para uma conta destino
        a partir do nome de usuario
        """
        result: bool = False
        if account is not None and destination is not None:
            result = account.__transfer(value, destination, self.log)
        return result

    def __str__(self):
        return f"Name: {self.__name}\n"
