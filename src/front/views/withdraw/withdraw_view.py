import flet as ft
from flet import (
    Column,
    Row,
    Text,
    TextField,
    Container,
    MainAxisAlignment,
    CrossAxisAlignment,
    colors,
    ElevatedButton,
    icons,
    Icon,
)

from ...constants import routes
from ....back.controllers.client_front_controller import ClientFrontController


def withdrawView(page: ft.Page, client: ClientFrontController):
    result = client.loggedAccountInfos()
    account = result['account']
    person = result['person']

    limit = account['limit']
    balance = account['balance']

    textFieldValue = TextField(
        label="Valor:",
        border_color=colors.SECONDARY,
    )

    def onWithdraw(e):
        if (textFieldValue.value is not None):
            value = float(textFieldValue.value)

            result = client.withdraw(value)

            if result:
                page.snack_bar = ft.SnackBar(
                    Row([
                        Icon(icons.CHECK, color=colors.ON_SECONDARY),
                        Text(
                            "Saque realizado com sucesso!",
                            color=colors.ON_SECONDARY,
                        ),
                    ]),
                    bgcolor=colors.SECONDARY_CONTAINER,
                )
                page.snack_bar.open = True
                page.go(routes.DASHBOARD_VIEW)
            else:
                print("Erro ao realizar saque!")
                page.snack_bar = ft.SnackBar(
                    Row([
                        Icon(icons.ERROR, color=colors.ON_ERROR),
                        Text(
                            "Erro ao realizar saque!",
                            color=colors.ON_ERROR,
                        ),
                    ]),
                    bgcolor=colors.ERROR_CONTAINER,
                )
                page.snack_bar.open = True
                page.update()

    return ft.View(
        routes.WITHDRAW_VIEW,
        [
            Column(
                [
                    Column([
                        Text(f"User: {account['accountName']}"),
                        Text(
                            f"Name: {person['firstName']} {person['lastName']}"
                        ),
                        Text(f"CPF: {person['cpf']}"),
                        Text(f"Balance: R$ {balance}/R$ {limit}"),
                    ]),
                    Container(height=20),
                    textFieldValue,
                    ElevatedButton(
                        text="Sacar!".upper(),
                        icon=icons.ADD,
                        on_click=onWithdraw,
                    ),
                ],
                wrap=True,
                horizontal_alignment=CrossAxisAlignment.CENTER,
            ),
        ],
        appbar=ft.AppBar(
            title=Text("Operação de Saque"),
            center_title=True,
            bgcolor=colors.SURFACE_VARIANT,
        ),
        vertical_alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
    )
