import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
            rx.avatar(name="Hector Barrios"),
            rx.text("@barrioshector"),
            rx.text("Hola mi nombre es Hector Manuel Barrios")
    )
