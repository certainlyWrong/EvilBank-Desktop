import json


class ClientModel:

    def __init__(
        self,
        firstName,
        lastName,
        age,
        cpf,
        accountName,
        balance,
        limit,
    ) -> None:
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.cpf = cpf
        self.accountName = accountName
        self.balance = balance
        self.limit = limit

    def toDict(self):
        return {
            'firstName': self.firstName,
            'lastName': self.lastName,
            'age': self.age,
            'cpf': self.cpf,
            'accountName': self.accountName,
            'balance': self.balance,
            'limit': self.limit,
        }

    def toJson(self):
        return json.dumps(self.toDict())

    def fromDict(self, dict):
        return ClientModel(
            dict['firstName'],
            dict['lastName'],
            dict['age'],
            dict['cpf'],
            dict['accountName'],
            dict['balance'],
            dict['limit'],
        )

    def fromJson(self, json):
        return self.fromDict(json.loads(json))
