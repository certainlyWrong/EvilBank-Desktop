import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

from ..models.log_model import LogModel, LogEntity
from ..models.person_model import PersonModel, PersonEntity
from ..models.account_model import AccountModel, AccountEntity
from ..entities import Base


class BankController:

    def __init__(
        self,
        name: str,
        agency: str,
        engine: sa.engine.Engine,
    ):
        self.__name = name
        self.__agency = agency
        self.__engine = engine
        self.__connection = engine.connect()
        self.__session = sessionmaker(bind=self.__connection)()

    @classmethod
    def factoryBanckController(cls, name: str, agency: str):

        dataBaseName = name.lower().replace(' ', '')

        engine = sa.create_engine(
            'mysql+mysqlconnector://root:123456@localhost:3306')
        engine.execute(f'CREATE DATABASE IF NOT EXISTS {dataBaseName}')
        engine = sa.create_engine(
            f'mysql+mysqlconnector://root:123456@localhost:3306/{dataBaseName}'
        )

        Base.metadata.create_all(engine)

        return cls(name, agency, engine)

    def dispose(self):
        self.__engine.execute('DROP DATABASE IF EXISTS evilofbanktest')
        self.__session.close()
        self.__connection.close()
        self.__engine.dispose()

    def createAccount(
        self,
        personFirstName: str,
        personLastName: str,
        age: int,
        cpf: str,
        accountName: str,
        accountPassword: str,
        accountBalance: float,
        accountLimit: float,
        commit: bool = False,
    ):
        result = None

        if (not personFirstName.isnumeric() and len(personFirstName) > 10
                and len(personFirstName) < 255 and cpf.isnumeric()
                and len(cpf) == 11 and not accountName.isalpha()
                and self.checkAccountNameExists(accountName) is False):

            person = self.createPerson(
                personFirstName,
                personLastName,
                age,
                cpf,
                commit,
            )

            if person is not None:
                account = AccountModel.factoryAccountModel(
                    person.personId,
                    accountName,
                    accountPassword,
                    accountBalance,
                    accountLimit,
                )

                if commit and account is not None:
                    saveResult = self.__saveEntity(account.toEntity())

                    if saveResult:
                        result = account
                elif account is not None:
                    result = account

        return result

    def createPerson(self,
                     firstName: str,
                     lastName: str,
                     age: int,
                     cpf: str,
                     commit: bool = False):
        result = None

        if (not firstName.isalpha() and not lastName.isalpha()
                and cpf.isnumeric() and isinstance(age, int)):

            person = PersonModel.create(
                firstName=firstName,
                lastName=lastName,
                age=age,
                cpf=cpf,
            )

            if commit and person is not None:
                personEntity = person.toEntity()
                saveResult = self.__saveEntity(personEntity)
                if saveResult:
                    result = person
            elif person is not None:
                result = person

        return result

    def accountByLogin(self, accountName: str, accountPassword: str):
        result = None

        try:
            accountResult = self.__session.query(AccountEntity).filter(
                AccountEntity.account_name == accountName,
                AccountEntity.account_password == accountPassword,
            ).one()

            result = AccountModel.fromEntity(accountResult)
        except Exception as e:
            print(e)

        return result

    def accountById(self, accountId: str):
        result = None

        try:
            accountResult = self.__session.query(AccountEntity).filter(
                AccountEntity.account_id == accountId, ).one()

            result = AccountModel.fromEntity(accountResult)
        except Exception as e:
            print(e)

        return result

    # TODO: testar
    def personByCpf(self, cpf: str):
        result = None

        try:
            personResult = self.__session.query(PersonEntity).filter(
                PersonEntity.person_cpf == cpf, ).one()

            result = PersonModel.fromEntity(personResult)
        except Exception as e:
            print(e)

        return result

    # TODO: testar
    def accountByPersonId(self, personId: int):
        result = None

        try:
            accountResult = self.__session.query(AccountEntity).filter(
                AccountEntity.person_id == personId, ).one()

            result = AccountModel.fromEntity(accountResult)
        except Exception as e:
            print(e)

        return result

    def checkAccountNameExists(self, accountName: str):
        result = False

        try:
            accountResult = self.__session.query(AccountEntity).filter(
                AccountEntity.account_name == accountName, ).one()

            if accountResult is not None:
                result = True
        except Exception as e:
            print(e)

        return result

    # TODO: testar
    def checkAccountNameExistsByPersonId(self, accountName: str):
        result = False

        try:
            accountResult = self.__session.query(AccountEntity).filter(
                AccountEntity.account_name == accountName, ).one()

            if accountResult is not None:
                result = True
        except Exception as e:
            print(e)

        return result

    def __saveEntity(self, entity: Base) -> bool:
        result = False

        try:
            self.__session.add(entity)
            self.__session.commit()
            result = True
        except Exception as e:
            self.__session.rollback()
            print(e)

        return result

    def __repr__(self):
        return f'BankController(name={self.__name}, agency={self.__agency})'
