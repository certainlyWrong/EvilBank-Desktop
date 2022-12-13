class Cliente:
    def __init__(self, nome: str, sobrenome: str, cpf: str) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def __equals__(self, other: "Cliente") -> bool:
        return (
            self.nome == other.nome and
            self.sobrenome == other.sobrenome and
            self.cpf == other.cpf
        )
