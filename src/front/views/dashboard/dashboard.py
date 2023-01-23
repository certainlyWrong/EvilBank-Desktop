import flet as ft
from flet import (
    Column,
    Row,
    Card,
    GridView,
    ElevatedButton,
    Text,
    Container,
    MainAxisAlignment,
    CrossAxisAlignment,
    colors,
    icons,
    ScrollMode,
)

from ...constants import routes
from ....back.controllers.client_front_controller import ClientFrontController


def dashboardView(page: ft.Page, client: ClientFrontController):

    result = client.loggedAccountInfos()

    logs = result['logs']
    account = result['account']
    person = result['person']

    return ft.View(
        routes.DASHBOARD_VIEW,
        [
            Column(
                [
                    Text(
                        "Usuário".upper(),
                        color=colors.PRIMARY,
                        size=20,
                    ),
                    Text("Usuário: " + account['accountName']),
                    Text(
                        "Nome: " + person['firstName'] + ' ' +
                        person['lastName'], ),
                    Text("CPF: " + person['cpf']),
                    Text("Balance: " + str(account['balance']) + ' / ' +
                         "Limit: " + str(account['limit'])),
                ],
                wrap=True,
                horizontal_alignment=CrossAxisAlignment.CENTER,
            ),
            GridView(
                [
                    ElevatedButton(
                        "Saque",
                        icon=icons.WALLET,
                        on_click=lambda e: page.go(routes.WITHDRAW_VIEW),
                    ),
                    ElevatedButton(
                        "Depósito",
                        icon=icons.WALLET,
                        on_click=lambda e: page.go(routes.DEPOSIT_VIEW),
                    ),
                    ElevatedButton(
                        "Transferência",
                        icon=icons.PERSON,
                        on_click=lambda e: page.go(routes.TRANSFER_VIEW),
                    ),
                ],
                padding=10,
                spacing=10,
                width=500,
                col=3,
                max_extent=150,
            ),
            Text(
                "Histórico".upper(),
                color=colors.PRIMARY,
                size=20,
            ),
            Column(
                [
                    Card(
                        Container(
                            Row([
                                Column([
                                    Text(f"Data: {log['logDate']}"),
                                    Text(f"Tipo: {log['logType']}"),
                                    Text(f"Valor: {log['logMessage']}"),
                                ])
                            ]),
                            margin=10,
                        ),
                        margin=10,
                        elevation=2,
                    ) for log in logs
                ],
                width=300,
            ),
        ],
        appbar=ft.AppBar(
            title=Text("Dashboard"),
            center_title=True,
            bgcolor=colors.SURFACE_VARIANT,
            actions=[
                Container(
                    ElevatedButton(
                        "Sair",
                        icon=icons.LOGOUT,
                        on_click=lambda e: page.go(routes.HOME_VIEW),
                    ),
                    padding=10,
                ),
            ]),
        vertical_alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
        scroll=ScrollMode.ADAPTIVE,
    )
