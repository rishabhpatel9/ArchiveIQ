import reflex as rx
from rxconfig import config

class GlobalState(rx.State):
    # The app state.
    notebooks: list[str] = ["Research on AI Agents", "Project ArchiveIQ Docs", "Machine Learning Notes"]
    show_settings: bool = False
    
    # New settings
    notebook_view_mode: str = "Per Notebook"
    global_view_style: str = "Image+Title"

    def toggle_settings(self):
        self.show_settings = not self.show_settings

def settings_dialog() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.content(
            rx.dialog.title("Settings", text_align="center"),
            rx.divider(mt="4", mb="6"),
            rx.vstack(
                rx.hstack(
                    rx.text("Notebooks Tile View", width="280px"),
                    rx.select(
                        ["Per Notebook", "Apply to all"],
                        value=GlobalState.notebook_view_mode,
                        on_change=GlobalState.set_notebook_view_mode,
                    ),
                    width="100%",
                    align="center",
                    justify="between",
                ),
                rx.cond(
                    GlobalState.notebook_view_mode == "Apply to all",
                    rx.hstack(
                        rx.text("Global View Style", width="280px"),
                        rx.select(
                            ["Image+Title", "Title"],
                            value=GlobalState.global_view_style,
                            on_change=GlobalState.set_global_view_style,
                        ),
                        width="100%",
                        align="center",
                        justify="between",
                    ),
                ),
                rx.hstack(
                    rx.text("Notebooks Library Path", width="280px"),
                    rx.input(placeholder="/path/to/your/documents", width="100%"),
                    width="100%",
                    align="center",
                    justify="between",
                ),
                rx.hstack(
                    rx.text("LLM Provider"),
                    rx.select(
                        ["LM Studio", "Ollama"],
                        default_value="LM Studio",
                    ),
                    width="100%",
                    justify="between",
                ),
                rx.hstack(
                    rx.text("LLM API Endpoint", width="280px"),
                    rx.input(placeholder="http://localhost:1234", width="100%"),
                    width="100%",
                    align="center",
                    justify="between",
                ),
                rx.hstack(
                    rx.text("Default LLM"),
                    rx.hstack(
                        rx.button(
                            rx.icon("rotate-cw"),
                            variant="ghost",
                            size="1",
                            cursor="pointer",
                            on_click=lambda: rx.window_alert("Syncing models..."),
                        ),
                        rx.select(
                            ["Detect Models", "Qwen3.5-2B", "Qwen3.5-9B", "Qwen3.5-0.8B"],
                            default_value="Detect Models",
                        ),
                        spacing="3",
                        align="center",
                    ),
                    width="100%",
                    justify="between",
                    align="center",
                ),
                spacing="4",
                width="100%",
            ),
            rx.box(height="1em"),
            rx.hstack(
                rx.dialog.close(
                    rx.button("Save Changes", color_scheme="indigo"),
                ),
                rx.dialog.close(
                    rx.button("Cancel", variant="soft", color_scheme="gray"),
                ),
                justify="end",
                spacing="3",
            ),
        ),
        open=GlobalState.show_settings,
        on_open_change=GlobalState.toggle_settings,
    )

def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.menu.root(
                rx.menu.trigger(
                    rx.button(
                        rx.icon("settings"),
                        variant="soft",
                        color_scheme="gray",
                        size="2",
                        cursor="pointer",
                    ),
                ),
                rx.menu.content(
                    rx.menu.item(
                        rx.hstack(
                            rx.icon("moon", size=16),
                            rx.text("Dark Mode"),
                            rx.spacer(),
                            rx.switch(
                                checked=rx.color_mode == "dark",
                                on_change=rx.toggle_color_mode,
                            ),
                            width="100%",
                        ),
                        close_on_select=False,
                    ),
                    rx.menu.separator(),
                    rx.menu.item(
                        rx.hstack(
                            rx.icon("sliders-vertical", size=16),
                            rx.text("Settings"),
                        ),
                        on_click=GlobalState.toggle_settings,
                    ),
                ),
            ),
            position="fixed",
            top="1.5em",
            right="2em",
            z_index="100",
        )
    )

def index() -> rx.Component:
    return rx.box(
        navbar(),
        settings_dialog(),
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

