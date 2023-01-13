import flet as ft
from flet import (
    Column,
    Text,
    TextField,
    MainAxisAlignment,
    CrossAxisAlignment,
    colors,
    ElevatedButton,
    Container,
    ListView,
    icons,
    ScrollMode,
)

from ...constants import routes

from ....back.controllers.bank_controller import BankController
from ...components.image_header_component import imageHeaderComponent
from ...components.account_card_component import accountCardComponent


def searchAccountView(page: ft.Page, bank: BankController):

    textFieldUserName = TextField(
        label="Nome:",
        border_color=colors.SECONDARY,
    )

    users = []

    def addAccount(e):
        if (textFieldUserName is not None):

            name = textFieldUserName.value
            textFieldUserName.value = ""
            if name is not None:
                for account in bank.accountByClientFirstName(name):
                    users.append(accountCardComponent(account))

        page.update()

    return ft.View(
        routes.INSERT_ACCOUNT_VIEW,
        [
            imageHeaderComponent(),
            Column(
                [
                    textFieldUserName,
                    ElevatedButton(
                        text="BUSCAR".upper(),
                        icon=icons.SEARCH,
                        on_click=addAccount,
                    ),
                    Container(
                        ListView(users),
                        width=500,
                    ),
                ],
                wrap=True,
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
            )
        ],
        appbar=ft.AppBar(
            title=Text("Buscar usuários!"),
            center_title=True,
            bgcolor=colors.SURFACE_VARIANT,
        ),
        horizontal_alignment=CrossAxisAlignment.CENTER,
        scroll=ScrollMode.ADAPTIVE,
    )
