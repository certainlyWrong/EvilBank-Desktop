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
from ....back.models.person_model import PersonModel
from ....back.models.account_model import AccountModel
from ....back.controllers.bank_controller import BankController


def depositView(page: ft.Page, bank: BankController):

    account = AccountModel.empty()
    person = PersonModel.empty()

    if (bank.loggedAccount is not None and bank.loggedPerson is not None):
        person = bank.loggedPerson
        account = bank.loggedAccount

    textFieldValue = TextField(
        label="Valor:",
        border_color=colors.SECONDARY,
    )

    def onDeposit(e):
        if (textFieldValue.value is not None):

            result = False

            value = float(textFieldValue.value)

            if bank.loggedAccount is not None:
                result = bank.deposit(bank.loggedAccount, value)

            if result:
                page.snack_bar = ft.SnackBar(
                    Row([
                        Icon(icons.CHECK, color=colors.ON_SECONDARY),
                        Text(
                            "Depósito realizado com sucesso!",
                            color=colors.ON_SECONDARY,
                        ),
                    ]),
                    bgcolor=colors.SECONDARY_CONTAINER,
                )
                page.snack_bar.open = True
                page.go(routes.DASHBOARD_VIEW)
            else:
                print("Erro ao realizar depósito!")
                page.snack_bar = ft.SnackBar(
                    Row([
                        Icon(icons.ERROR, color=colors.ON_ERROR),
                        Text(
                            "Erro ao realizar depósito!",
                            color=colors.ON_ERROR,
                        ),
                    ]),
                    bgcolor=colors.ERROR_CONTAINER,
                )
                page.snack_bar.open = True
                page.update()

    return ft.View(
        routes.DEPOSIT_VIEW,
        [
            Column(
                [
                    Column([
                        Text(f"User: {account.accountName}"),
                        Text(f"Name: {person.firstName} {person.lastName}"),
                        Text(f"CPF: {person.cpf}"),
                        Text(
                            f"Balance: R$ {account.balance}/R$ {account.limit}"
                        ),
                    ]),
                    Container(height=20),
                    textFieldValue,
                    ElevatedButton(
                        text="Depositar".upper(),
                        icon=icons.ADD,
                        on_click=onDeposit,
                    ),
                ],
                wrap=True,
                horizontal_alignment=CrossAxisAlignment.CENTER,
            ),
        ],
        appbar=ft.AppBar(
            title=Text("Operação de Depósito"),
            center_title=True,
            bgcolor=colors.SURFACE_VARIANT,
        ),
        vertical_alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
    )
