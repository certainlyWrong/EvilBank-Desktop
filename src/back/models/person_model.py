from uuid import uuid4

from ..entities.person_entity import PersonEntity


class PersonModel:

    def __init__(
        self,
        personId: str,
        firstName: str,
        lastName: str,
        age: int,
        cpf: str,
    ):
        self.__personId = personId
        self.__firstName = firstName
        self.__lastName = lastName
        self.__age = age
        self.__cpf = cpf

    @classmethod
    def create(
        cls,
        firstName: str,
        lastName: str,
        age: int,
        cpf: str,
    ):
        result = None

        # validar cpf, age, personName
        if cpf.isnumeric() or len(cpf) != 11:
            if not firstName.isalpha():
                if isinstance(age, int):
                    result = cls(
                        str(uuid4()),
                        firstName,
                        lastName,
                        age,
                        cpf,
                    )

        return result

    @classmethod
    def fromEntity(cls, personEntity: PersonEntity) -> 'PersonModel':
        return cls(
            personEntity.person_id,  # type: ignore
            personEntity.person_first_name,  # type: ignore
            personEntity.person_last_name,  # type: ignore
            personEntity.person_age,  # type: ignore
            personEntity.person_cpf,  # type: ignore
        )

    def toEntity(self) -> PersonEntity:
        return PersonEntity(
            person_id=self.personId,
            person_first_name=self.firstName,
            person_last_name=self.lastName,
            person_age=self.age,
            person_cpf=self.cpf,
        )

    @property
    def personId(self) -> str:
        return self.__personId

    @property
    def firstName(self) -> str:
        return self.__firstName

    def lastName(self) -> str:
        return self.__lastName

    @property
    def age(self) -> int:
        return self.__age

    @property
    def cpf(self) -> str:
        return self.__cpf
