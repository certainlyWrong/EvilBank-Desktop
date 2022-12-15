class PersonModel:

    __slots__ = [
        "firstName",
        "lastName",
        "cpf",
    ]

    def __init__(self, firstName: str, last_name: str, cpf: str) -> None:
        self.firstName = firstName
        self.lastName = last_name
        self.cpf = cpf

    def __equals__(self, other: "PersonModel") -> bool:
        return (
            self.firstName == other.firstName
            and self.lastName == other.lastName
            and self.cpf == other.cpf
        )
