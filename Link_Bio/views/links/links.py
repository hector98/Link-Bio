import reflex as rx
from Link_Bio.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
            link_button("GitHub", "https://github.com/hector98"),
            link_button("Linkedin", "https://www.linkedin.com/in/h%C3%A9ctor-manuel-b-3960b2117/"),
            #link_button("Email"),
            link_button("Twitter", "https://x.com/barrioshector13")
    )
