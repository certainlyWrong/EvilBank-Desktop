import flet as ft
from flet import (
    Row,
    Container,
    icons,
    ElevatedButton,
)

from ...constants import routes
from .components.header_componet import headerComponent


def homeView(page: ft.Page):
    return ft.View(
        routes.HOME_VIEW,
        [
            headerComponent,
            Container(height=20),
            Row(
                [
                    ElevatedButton(
                        "criar conta".upper(),
                        icon=icons.ADD,
                        on_click=lambda e: page.go(routes.INSERT_ACCOUNT_VIEW),
                    ),
                    ElevatedButton(
                        "entrar".upper(),
                        icon=icons.LOGIN,
                        on_click=lambda e: page.go(routes.LOGIN_VIEW, ),
                    ),
                ],
                width=500,
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
            ),
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
