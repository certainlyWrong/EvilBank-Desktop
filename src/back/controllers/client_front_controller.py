import json
import socket


class ClientController:

    def __init__(self, client):
        self.__client: socket.socket = client
        self.__buffer_size = 1024

        self.user = None

    @classmethod
    def factoryHostAndPort(cls, host: str, port: int):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))

        return cls(client)

    def register(
        self,
        firstName: str,
        lastName: str,
        cpf: str,
        age: int,
        accountName: str,
        passWord: str,
    ):
        self.send({
            'command': 'register',
            'firstName': firstName,
            'lastName': lastName,
            'cpf': cpf,
            'age': age,
            'accountName': accountName,
            'passWord': passWord,
        })

        return self.receive()

    def login(self, accountName: str, passWord: str):
        self.send({
            'command': 'login',
            'accountName': accountName,
            'passWord': passWord,
        })
        result = self.receive()

        return result['status'] == 'success'

    def deposit(self, value: float):
        self.send({
            'command': 'deposit',
            'value': value,
        })
        return self.receive()['status'] == 'success'

    def withdraw(self, value: float):
        self.send({
            'command': 'withdraw',
            'value': value,
        })
        return self.receive()['status'] == 'success'

    def transfer(self, accountName: str, value: float):
        self.send({
            'command': 'transfer',
            'accountName': accountName,
            'value': value,
        })
        return self.receive()['status'] == 'success'

    def loggedAccountInfos(self):
        self.send({'command': 'loggedAccountInfos'})
        return self.receive()

    def start(self):
        while True:
            data = input('Digite o comando: ')

            if data == 'exit':
                break

            self.send({'command': data})

            print(self.receive())

    def close(self):
        self.send({'command': 'exit'})
        self.__client.close()

    def send(self, data):
        # Envia um json em pacotes de 1024 bytes
        # "end" é uma flag que indica o fim da mensagem

        dataStr = json.dumps(data)

        for i in range(0, len(dataStr), self.__buffer_size):
            self.__client.send(dataStr[i:i +
                                       self.__buffer_size].encode('utf-8'))

        self.__client.send('end'.encode('utf-8'))

    def receive(self):
        # Recebe um json em pacotes de 1024 bytes
        # "end" é uma flag que indica o fim da mensagem

        data = ''

        while True:
            data += self.__client.recv(self.__buffer_size).decode('utf-8')
            if data[-3:] == 'end':
                break
        data = data[:-3]
        return json.loads(data)


if __name__ == '__main__':
    client_controller = ClientController.factoryHostAndPort('localhost', 8080)

    client_controller.start()
