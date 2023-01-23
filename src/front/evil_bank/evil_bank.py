import atexit

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
    # SEARCH_ACCOUNT_VIEW,
    LOGIN_VIEW,
    DASHBOARD_VIEW,
    WITHDRAW_VIEW,
    DEPOSIT_VIEW,
    TRANSFER_VIEW,
)

from ...back.controllers.client_front_controller import ClientController

from ..views.home.home_view import homeView
from ..views.register_account.register_account_view import (
    registerAccountView, )
from ..views.dashboard.dashboard import dashboardView
# from ..views.search_account.search_account_view import searchAccountView
from ..views.withdraw.withdraw_view import withdrawView
from ..views.deposit.deposit_view import depositView
from ..views.transfer.transfer_view import transferView
from ..views.login.login_view import loginView


def evilBankApp(page: ft.Page):
    page.title = "Evil Bank"

    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.theme_mode = ThemeMode.SYSTEM

    page.theme = Theme(color_scheme_seed=colors.PURPLE)
    page.dark_theme = Theme(color_scheme_seed=colors.PURPLE)

    clientController = ClientController.factoryHostAndPort("localhost", 8000)

    def close_handler():
        print("Closing client\n\n")
        clientController.close()
        page.close()

    atexit.register(close_handler)

    def route_change(route):
        if page.route == HOME_VIEW:
            page.views.clear()
            page.views.append(homeView(page))

        if page.route == INSERT_ACCOUNT_VIEW:
            page.views.append(registerAccountView(page, clientController))

        # if page.route == SEARCH_ACCOUNT_VIEW:
        #     page.views.append(searchAccountView(page, bank))

        if page.route == LOGIN_VIEW:
            page.views.append(loginView(page, clientController))

        if page.route == DASHBOARD_VIEW:
            page.views.clear()
            page.views.append(dashboardView(page, clientController))

        if page.route == WITHDRAW_VIEW:
            page.views.append(withdrawView(page, clientController))

        if page.route == DEPOSIT_VIEW:
            page.views.append(depositView(page, clientController))

        if page.route == TRANSFER_VIEW:
            page.views.append(transferView(page, clientController))

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    def close():
        print("Closing client\n\n")
        clientController.close()
        page.close()

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.on_close = close
    page.go(page.route)
