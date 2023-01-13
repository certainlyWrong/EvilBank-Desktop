import flet as ft
from flet import (
    Row,
    Image,
    Text,
    Column,
    colors,
    Container,
)

import json

headerTextInfo = ""

with open("assets/infos/homeInfos.json", "r") as f:
    headerTextInfo = json.load(f)["homeTextIntro"]

headerComponent = Container(
    Column(
        [
            Text(
                "Evil Bank",
                size=60,
                color=colors.PRIMARY,
            ),
            Container(height=20),
            Row(
                [
                    Text(
                        headerTextInfo,
                        size=15,
                        color=colors.SECONDARY,
                        text_align=ft.TextAlign.LEFT,
                    ),
                    Container(width=20),
                    Image(
                        'assets/images/pngegg.png',
                        height=150,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    ))
