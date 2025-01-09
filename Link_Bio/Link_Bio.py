"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

from Link_Bio.components.navbar import navbar
from Link_Bio.views.header.header import header
from Link_Bio.views.links.links import links
from Link_Bio.components.footer import footer

class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.vstack(
            header(),
            navbar(),
            links(),
            footer()
    )


app = rx.App()
app.add_page(index)
