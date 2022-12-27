import unittest
from time import sleep

import src.back as back

bank = back.BankController.factoryBanckController(
    'Evil Of Bank Test',
    '1234',
)


class TestBank(unittest.TestCase):

    @classmethod
    def tearDownClass(cls):
        sleep(2)
        bank.dispose()
        super().tearDownClass()

    def test_createAccount(self):
        result = bank.createAccount(
            'Evil Of Bank',
            21,
            '12345678901',
            'evil1',
            '1234',
            999.995,
            1000,
            commit=True,
        )

        self.assertIsNotNone(result)

        if result is not None:
            self.assertTrue(result.accountName == 'evil1')
            self.assertTrue(result.password == '1234')
            self.assertTrue(result.balance == 999.995)
            self.assertTrue(result.limit == 1000)

    def test_createAccountCPFFail(self):
        bank.createAccount(
            'Maria',
            ''
            23,
            '54321098765',
            'maria1',
            '1234',
            1000,
            1000,
            commit=True,
        )

        result = bank.createAccount(
            'Maria da Silva',
            23,
            '54321098765',
            'maria2',
            '1234',
            1000,
            1000,
            commit=True,
        )

        self.assertIsNone(result)

    def test_createAccountNameFail(self):

        result1 = bank.createAccount(
            'Maria de Sousa',
            23,
            '54321098765',
            'maria1',
            '1234',
            1000,
            1000,
            commit=True,
        )

        result2 = bank.createAccount(
            'Maria da Silva',
            23,
            '54321098762',
            'maria1',
            '1234',
            1000,
            1000,
            commit=True,
        )

        self.assertIsNotNone(result1)
        self.assertIsNone(result2)

    def test_createPerson(self):
        result = bank.createPerson(
            'Evil Of Bank',
            21,
            '87123456789',
            commit=True,
        )

        self.assertIsNotNone(result)

        if result is not None:
            self.assertTrue(result.personName == 'Evil Of Bank')
            self.assertTrue(result.age == 21)
            self.assertTrue(result.cpf == '87123456789')

    def test_createPersonCPFFail(self):
        result = bank.createPerson(
            'Evil Of Bank',
            21,
            '32165498701',
            commit=True,
        )

        result = bank.createPerson(
            'Evil Of Bank',
            21,
            '32165498701',
            commit=True,
        )

        self.assertIsNone(result)

    def test_createPersonNameFail(self):
        result = bank.createPerson(
            'Evil',
            21,
            '12345678902',
            commit=True,
        )

        self.assertIsNone(result)

    def test_checkAccountNameExists(self):
        bank.createAccount(
            'Pedro da Silva',
            21,
            '76543210987',
            'pedro1',
            '1234',
            999.995,
            1000,
            commit=True,
        )

        result = bank.checkAccountNameExists('pedro1')

        self.assertTrue(result)

    def test_accountByLogin(self):
        bank.createAccount(
            'João da Silva',
            21,
            '54321098765',
            'joao1',
            '1234',
            999.995,
            1000,
            commit=True,
        )

        result = bank.accountByLogin('joao1', '1234')

        self.assertIsNotNone(result)

        if result is not None:
            self.assertTrue(result.accountName == 'joao1')
            self.assertTrue(result.password == '1234')
            self.assertTrue(result.balance == 999.995)
            self.assertTrue(result.limit == 1000)

    def test_accountByLoginFail(self):
        result = bank.accountByLogin('joao3', '12345')

        self.assertIsNone(result)

    def test_accountByLoginFail2(self):
        result = bank.accountByLogin('joao3', '1234')

        self.assertIsNone(result)

    def test_accountById(self):
        account = bank.createAccount(
            'Texugo da Silva',
            21,
            '65789012345',
            'texugo1',
            '1234',
            999.995,
            1000,
            commit=True,
        )

        if account is not None:
            result = bank.accountById(account.accountId)

            self.assertIsNotNone(result)

            if result is not None:
                self.assertTrue(result.accountName == 'texugo1')
                self.assertTrue(result.password == '1234')
                self.assertTrue(result.balance == 999.995)
                self.assertTrue(result.limit == 1000)

    def test_accountByIdFail(self):
        result = bank.accountById('123')

        self.assertIsNone(result)

    def test_personByCpf(self):
        bank.createAccount(
            'Avelar da Silva',
            21,
            '57321098765',
            'avelar1',
            '1234',
            999.995,
            1000,
            commit=True,
        )

        result = bank.personByCpf('57321098765')

        self.assertIsNotNone(result)
