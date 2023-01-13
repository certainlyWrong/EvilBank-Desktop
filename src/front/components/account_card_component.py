import flet as ft
from flet import (
    Text,
    Card,
    Column,
    Row,
    icons,
    Icon,
    Container,
)

from ...back.models.account_model import AccountModel


def accountCardComponent(account: AccountModel) -> Card:

    return Card(
        Container(
            Row(
                [
                    Column(
                        [
                            Text(
                                "Nome: " + account.client.firstName + " " +
                                account.client.lastName,
                                size=20,
                            ),
                            Text("CPF: " + account.client.cpf),
                            Text("Usuário: " + account.user),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                    ),
                    Icon(icons.ACCOUNT_CIRCLE),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=10,
        ),
        margin=10,
        elevation=5,
    )
