import flet as ft
from flet import (
    colors,
    MainAxisAlignment,
    CrossAxisAlignment,
    Theme,
    ThemeMode,
)

from ..constants.routes import (
    HOME_VIEW,
    INSERT_ACCOUNT_VIEW,
    SEARCH_ACCOUNT_VIEW,
    LOGIN_VIEW,
    DASHBOARD_VIEW,
    WITHDRAW_VIEW,
    DEPOSIT_VIEW,
    TRANSFER_VIEW,
)

from ..views.home.home_view import homeView
from ..views.dashboard.dashboard import dashboardView
from ..views.register_account.register_account_view import (
    registerAccountView, )
from ..views.search_account.search_account_view import searchAccountView
from ..views.withdraw.withdraw_view import withdrawView
from ..views.deposit.deposit_view import depositView
from ..views.transfer.transfer_view import transferView
from ..views.login.login_view import loginView

from ...back.controllers.bank_controller import BankController


def evilBankApp(page: ft.Page):
    page.title = "Evil Bank"

    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.theme_mode = ThemeMode.SYSTEM

    page.theme = Theme(color_scheme_seed=colors.PURPLE)
    page.dark_theme = Theme(color_scheme_seed=colors.PURPLE)

    bank = BankController.factorybankController(
        'evil bank',
        '1234',
    )

    def route_change(route):
        if page.route == HOME_VIEW:
            page.views.clear()
            page.views.append(homeView(page))

        if page.route == INSERT_ACCOUNT_VIEW:
            page.views.append(registerAccountView(page, bank))

        if page.route == SEARCH_ACCOUNT_VIEW:
            page.views.append(searchAccountView(page, bank))

        if page.route == LOGIN_VIEW:
            page.views.append(loginView(page, bank))

        if page.route == DASHBOARD_VIEW:
            page.views.clear()
            page.views.append(dashboardView(page, bank))

        if page.route == WITHDRAW_VIEW:
            page.views.append(withdrawView(page, bank))

        if page.route == DEPOSIT_VIEW:
            page.views.append(depositView(page, bank))

        if page.route == TRANSFER_VIEW:
            page.views.append(transferView(page, bank))

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    def close():
        bank.dispose()
        page.close()

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.on_close = close
    page.go(page.route)
