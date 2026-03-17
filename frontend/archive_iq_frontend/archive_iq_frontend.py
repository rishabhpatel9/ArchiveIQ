import reflex as rx
from rxconfig import config

class GlobalState(rx.State):
    # The app state.
    notebooks: list[str] = ["Research on AI Agents", "Project ArchiveIQ Docs", "Machine Learning Notes"]
    show_settings: bool = False
    
    # New settings
    notebook_view_mode: str = "Per Notebook"
    global_view_style: str = "Image+Title"

    def set_notebook_view_mode(self, mode: str | list[str]):
        if isinstance(mode, str):
            self.notebook_view_mode = mode

    def set_global_view_style(self, style: str | list[str]):
        if isinstance(style, str):
            self.global_view_style = style

    def toggle_settings(self):
        self.show_settings = not self.show_settings

def settings_dialog() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.content(
            rx.dialog.title("Settings", text_align="center"),
            rx.box(height="1em"),
            rx.vstack(
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
        rx.html("""
            <style>
                .rt-SegmentedControlItem[data-state='on'] {
                    background-color: var(--indigo-9) !important;
                    color: white !important;
                }
                .rt-SegmentedControlItem[data-state='on']:hover {
                    background-color: var(--indigo-10) !important;
                }
            </style>
        """),
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
                    # Quick Setting: Dark Mode
                    rx.box(
                        rx.hstack(
                            rx.icon("moon", size=15),
                            rx.text("Dark Mode", size="2"),
                            rx.spacer(),
                            rx.switch(
                                checked=rx.color_mode == "dark",
                                on_change=rx.toggle_color_mode,
                                size="1",
                            ),
                            width="100%",
                            align="center",
                        ),
                        padding_x="12px",
                        padding_y="8px",
                    ),
                    rx.menu.separator(),
                    # Quick Setting: View Modes
                    rx.box(
                        rx.vstack(
                            rx.hstack(
                                rx.icon("layout-grid", size=15),
                                rx.text("Notebooks View", size="2"),
                                rx.spacer(),
                                rx.segmented_control.root(
                                    rx.segmented_control.item("Per NB", value="Per Notebook"),
                                    rx.segmented_control.item("All", value="Apply to all"),
                                    value=GlobalState.notebook_view_mode,
                                    on_change=GlobalState.set_notebook_view_mode,
                                    size="1",
                                    color_scheme="indigo",
                                    high_contrast=True,
                                ),
                                width="100%",
                                align="center",
                            ),
                            rx.cond(
                                GlobalState.notebook_view_mode == "Apply to all",
                                rx.hstack(
                                    rx.icon("palette", size=15),
                                    rx.text("Global Style", size="1"),
                                    rx.spacer(),
                                    rx.segmented_control.root(
                                        rx.segmented_control.item("Image", value="Image+Title"),
                                        rx.segmented_control.item("Text", value="Title"),
                                        value=GlobalState.global_view_style,
                                        on_change=GlobalState.set_global_view_style,
                                        size="1",
                                        color_scheme="indigo",
                                        high_contrast=True,
                                    ),
                                    width="100%",
                                    align="center",
                                    mt="1",
                                ),
                            ),
                            align_items="start",
                            width="100%",
                        ),
                        padding_x="12px",
                        padding_y="8px",
                    ),
                    rx.menu.separator(),
                    # Final Action: Full Settings
                    rx.menu.item(
                        rx.hstack(
                            rx.icon("sliders-vertical", size=15),
                            rx.text("Settings", size="2"),
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

def notebook_card(title: str) -> rx.Component:
    return rx.cond(
        GlobalState.global_view_style == "Image+Title",
        # Style 1: Image + Title (Card with Image at Top)
        rx.card(
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
                rx.text(title, weight="bold", size="3", mt="2"),
                rx.text("Last updated Mar 17, 2026", size="1", color=rx.color("gray", 10)),
                align="start",
                width="100%",
            ),
            width="100%",
            padding="1em",
            cursor="pointer",
            _hover={"transform": "translateY(-2px)", "transition": "transform 0.2s"},
        ),
        # Style 2: Title Only (Minimalist, like NotebookLM)
        rx.card(
            rx.vstack(
                rx.hstack(
                    rx.box(
                        rx.icon("book-text", size=24, color=rx.color("indigo", 9)),
                        padding="0.5em",
                        background=rx.color("indigo", 3),
                        border_radius="8px",
                    ),
                    width="100%",
                    align="center",
                ),
                rx.box(height="auto"),
                rx.heading(title, size="5", weight="bold", line_clamp=2),
                rx.spacer(),
                rx.hstack(
                    rx.text("Mar 17, 2026", size="1"),
                    rx.text("•", size="1"),
                    rx.text("3 sources", size="1"),
                    color=rx.color("gray", 10),
                    spacing="2",
                ),
                align="start",
                width="100%",
                height="150px",  # Fixed height for title-only cards
            ),
            variant="surface",
            width="100%",
            cursor="pointer",
            _hover={"background": rx.color("indigo", 2), "transition": "background 0.2s"},
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
                        notebook_card
                    ),
                    columns=rx.breakpoints(initial="1", sm="2", md="3", lg="4"),
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

