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

from ....back.controllers.client_front_controller import ClientController


def registerAccountView(page: ft.Page, clientController: ClientController):

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

            firstName = textFieldUserFirstName.value
            textFieldUserFirstName.value = ""

            lastName = textFieldUserLastName.value
            textFieldUserLastName.value = ""

            cpf = textFieldUserCPF.value
            textFieldUserCPF.value = ""

            age = textFieldUserAge.value
            textFieldUserAge.value = ""

            accountName = textFieldUserName.value
            textFieldUserName.value = ""

            passWord = textFieldUserPassword.value
            textFieldUserPassword.value = ""

            result = clientController.register(
                firstName,
                lastName,
                cpf,
                int(age),
                accountName,
                passWord,
            )

            if result['status'] == 'success':
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
                    open=True,
                )
            page.update()

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
