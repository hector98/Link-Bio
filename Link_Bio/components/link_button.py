import reflex as rx

def link_button(text: str, url: str) -> rx.Component:
    return rx.vstack(
            rx.button(text, href="https://github.com/hector98", is_external=True)
    )
