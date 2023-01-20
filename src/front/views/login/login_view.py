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
from ....back.controllers.bank_controller import BankController


def loginView(page: ft.Page, bank: BankController):

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
        if (textFieldUserName.value is not None
                and textFieldUserPassword.value is not None):
            user = textFieldUserName.value
            textFieldUserName.value = ""

            password = textFieldUserPassword.value
            textFieldUserPassword.value = ""

            result = bank.login(user, password)

            if result:
                page.snack_bar = ft.SnackBar(
                    Row([
                        Icon(icons.CHECK, color=colors.ON_SECONDARY),
                        Text(
                            "Login efetuado com sucesso!",
                            color=colors.ON_SECONDARY,
                        ),
                    ]),
                    bgcolor=colors.SECONDARY_CONTAINER,
                )
                page.snack_bar.open = True
                page.go(routes.DASHBOARD_VIEW)

            else:
                print("Usuário ou senha incorretos!")
                page.snack_bar = ft.SnackBar(
                    Row([
                        Icon(icons.CLOSE, color=colors.ON_SECONDARY),
                        Text(
                            "Usuário ou senha incorretos!",
                            color=colors.ON_SECONDARY,
                        ),
                    ]),
                    bgcolor=colors.SECONDARY_CONTAINER,
                    open=True,
                )
                # page.snack_bar.open = True
                page.update()

    return ft.View(
        routes.INSERT_ACCOUNT_VIEW,
        [
            Column(
                [
                    textFieldUserName,
                    textFieldUserPassword,
                    ElevatedButton(
                        text="Sign in".upper(),
                        icon=icons.ADD,
                        on_click=addAccount,
                    ),
                ],
                wrap=True,
                horizontal_alignment=CrossAxisAlignment.CENTER,
            ),
        ],
        appbar=ft.AppBar(
            title=Text("Entrar na conta!"),
            center_title=True,
            bgcolor=colors.SURFACE_VARIANT,
        ),
        vertical_alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
    )
