import reflex as rx

config = rx.Config(
    app_name="archive_iq_frontend",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)