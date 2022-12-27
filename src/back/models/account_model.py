from uuid import uuid4

from ..entities.account_entity import AccountEntity


class AccountModel:

    def __init__(
        self,
        accountId: str,
        personId: str,
        accountName: str,
        password: str,
        balance: float,
        limit: float,
    ):
        self.__accountId = accountId
        self.__personId = personId
        self.__accountName = accountName
        self.__password = password
        self.__balance = balance
        self.__limit = limit

    @classmethod
    def factoryAccountModel(
        cls,
        clientId: str,
        accountName: str,
        password: str,
        balance: float,
        limit: float,
    ):
        result = None

        if not accountName.isalpha():
            if not password.isalpha():
                if balance > 0:
                    if limit > 0:
                        result = cls(
                            str(uuid4()),
                            clientId,
                            accountName,
                            password,
                            balance,
                            limit,
                        )

        return result

    @classmethod
    def factoryEmpty(cls) -> 'AccountModel':
        return cls(
            str(uuid4()),
            str(uuid4()),
            '',
            '',
            0.0,
            0.0,
        )

    @classmethod
    def fromEntity(cls, accountEntity: AccountEntity) -> 'AccountModel':

        return cls(
            accountEntity.account_id,  # type: ignore
            accountEntity.person_id,  # type: ignore
            accountEntity.account_name,  # type: ignore
            accountEntity.account_password,  # type: ignore
            accountEntity.account_balance,  # type: ignore
            accountEntity.account_limit,  # type: ignore
        )

    def toEntity(self) -> AccountEntity:
        return AccountEntity(
            account_id=self.accountId,
            person_id=self.personId,
            account_name=self.accountName,
            account_password=self.password,
            account_balance=self.balance,
            account_limit=self.limit,
        )

    @property
    def accountId(self) -> str:
        return self.__accountId

    @property
    def personId(self) -> str:
        return self.__personId

    @property
    def accountName(self) -> str:
        return self.__accountName

    @accountName.setter
    def accountName(self, accountName: str | None) -> None:
        if accountName is not None:
            self.__accountName = accountName

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str | None) -> None:
        if password is not None:
            self.__password = password

    @property
    def balance(self) -> float:
        return self.__balance

    @property
    def limit(self) -> float:
        return self.__limit
