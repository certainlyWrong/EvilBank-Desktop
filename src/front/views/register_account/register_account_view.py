import hashlib

import flet as ft
from flet import (
    Column,
    Row,
    Text,
    TextField,
    MainAxisAlignment,
    CrossAxisAlignment,
    colors,
    ElevatedButton,
    icons,
    Icon,
)

from ...constants import routes

from ....back.models.person_model import PersonModel
from ....back.models.account_model import AccountModel
from ....back.controllers.bank_controller import BankController


def registerAccountView(page: ft.Page, bank: BankController):

    textFieldUserFirstName = TextField(
        label="Nome:",
        border_color=colors.SECONDARY,
    )
    textFieldUserLastName = TextField(
        label="Sobrenome:",
        border_color=colors.SECONDARY,
    )
    textFieldUserCPF = TextField(
        label="CPF:",
        # max_length=11,
        border_color=colors.SECONDARY,
    )

    textFieldUserAge = TextField(
        label="Idade:",
        # max_length=11,
        border_color=colors.SECONDARY,
    )

    textFieldUserName = TextField(
        label="Usuário:",
        border_color=colors.SECONDARY,
    )
    textFieldUserPassword = TextField(
        label="Senha:",
        password=True,
        border_color=colors.SECONDARY,
    )

    def addAccount(e):
        if (textFieldUserFirstName.value is not None
                and textFieldUserLastName.value is not None
                and textFieldUserCPF.value is not None
                and textFieldUserName.value is not None
                and textFieldUserPassword.value is not None
                and textFieldUserAge.value is not None):

            account = AccountModel.empty()
            person = PersonModel.empty()

            account.personId = person.personId

            person.firstName = textFieldUserFirstName.value
            textFieldUserFirstName.value = ""

            person.lastName = textFieldUserLastName.value
            textFieldUserLastName.value = ""

            person.cpf = textFieldUserCPF.value
            textFieldUserCPF.value = ""

            person.age = int(textFieldUserAge.value)
            textFieldUserAge.value = ""

            account.accountName = textFieldUserName.value
            textFieldUserName.value = ""

            account.hashAccount = hashlib.sha256(
                textFieldUserPassword.value.encode()).hexdigest()
            textFieldUserPassword.value = ""

            result1 = bank.saveEntity(person.toEntity())
            result2 = bank.saveEntity(account.toEntity())

            if result1 and result2:
                page.snack_bar = ft.SnackBar(
                    Row([
                        Icon(icons.CHECK, color=colors.ON_SECONDARY),
                        Text(
                            "Conta criada com sucesso!",
                            color=colors.ON_SECONDARY,
                        ),
                    ]),
                    bgcolor=colors.SECONDARY_CONTAINER,
                    open=True,
                )
                # page.snack_bar.open = True
                page.go(routes.HOME_VIEW)
            else:
                print("Erro ao criar conta!")
                page.snack_bar = ft.SnackBar(
                    Row([
                        Icon(icons.ERROR, color=colors.ON_ERROR),
                        Text(
                            "Usuário já existente!",
                            color=colors.ON_ERROR,
                        ),
                    ]),
                    bgcolor=colors.ERROR_CONTAINER,
                )
                page.snack_bar.open = True

    return ft.View(
        routes.INSERT_ACCOUNT_VIEW,
        [
            Column(
                [
                    textFieldUserFirstName,
                    textFieldUserLastName,
                    textFieldUserCPF,
                    textFieldUserAge,
                    textFieldUserName,
                    textFieldUserPassword,
                    ElevatedButton(
                        text="Cadastrar!".upper(),
                        icon=icons.ADD,
                        on_click=addAccount,
                    ),
                ],
                wrap=True,
                horizontal_alignment=CrossAxisAlignment.CENTER,
            ),
        ],
        appbar=ft.AppBar(
            title=Text("Cadastrar usuário!"),
            center_title=True,
            bgcolor=colors.SURFACE_VARIANT,
        ),
        vertical_alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
        # scroll=ScrollMode.ADAPTIVE,
    )
