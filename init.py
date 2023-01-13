import flet as ft
from src.front.evil_bank.evil_bank import evilBankApp

ft.app(
    target=evilBankApp,
    assets_dir="assets",
    host="0.0.0.0",
    port=5000,
)
