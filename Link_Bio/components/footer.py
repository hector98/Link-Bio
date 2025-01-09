import reflex as rx

def footer() -> rx.Component:
    return rx.vstack(
            rx.image(src="favicon.ico"),
            rx.link("GitHub", href="https://github.com/hector98"),
            rx.text("Hector Barrios")
            )
