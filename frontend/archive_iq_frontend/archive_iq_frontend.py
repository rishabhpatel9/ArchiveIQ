import reflex as rx
from rxconfig import config

class GlobalState(rx.State):
    # The app state.
    notebooks: list[str] = ["Research on AI Agents", "Project ArchiveIQ Docs", "Machine Learning Notes"]

def index() -> rx.Component:
    return rx.box(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            # Top Header
            rx.hstack(
                rx.button(
                    rx.icon("plus"),
                    "New Notebook",
                    color_scheme="indigo",
                    variant="solid",
                    size="3",
                    cursor="pointer",
                    on_click=lambda: rx.window_alert("Creating new notebook..."),
                ),
                width="100%",
                padding="2em",
                justify="start",
            ),
            
            # Recent Section
            rx.vstack(
                rx.heading("Recent Notebooks", size="5", weight="bold", mb="4"),
                rx.grid(
                    rx.foreach(
                        GlobalState.notebooks,
                        lambda nb: rx.card(
                            rx.vstack(
                                rx.box(
                                    rx.image(
                                        src="https://images.unsplash.com/photo-1481627834876-b7833e8f5570?auto=format&fit=crop&q=80&w=400&h=200",
                                        width="100%",
                                        height="120px",
                                        object_fit="cover",
                                        border_radius="8px",
                                    ),
                                    width="100%",
                                ),
                                rx.text(nb, weight="bold", size="3", mt="2"),
                                align="start",
                                width="100%",
                            ),
                            width="100%",
                            padding="1em",
                        )
                    ),
                    columns=rx.breakpoints(initial="1", sm="2", md="3"),
                    spacing="6",
                    width="100%",
                ),
                width="100%",
                padding_x="2em",
                align_items="start",
            ),
            width="100%",
            min_height="100vh",
            background="var(--slate-1)",
        ),
    )


app = rx.App(
    theme=rx.theme(
        appearance="dark",
        has_background=True,
        accent_color="indigo",
    ),
)
app.add_page(index, title="ArchiveIQ")
