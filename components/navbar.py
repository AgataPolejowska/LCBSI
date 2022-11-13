import dash_bootstrap_components as dbc
from dash import html


LCBSI_LOGO = "assets\\favicon\\favicon.ico"


class Navbar:
    def __init__(self):
        pass

    def get_layout(self):

        navbar = dbc.Navbar(
            dbc.Container(
                [
                    html.A(
                        dbc.Row(
                            [
                                dbc.Col(
                                    html.Img(
                                        src=LCBSI_LOGO,
                                        height="30px",
                                    )
                                ),
                                dbc.Col(
                                    dbc.NavbarBrand(
                                        "LCBSI",
                                        # change text spacing
                                        className="ml-2 text-white font-weight-bold fs-5",
                                    )
                                ),
                            ],
                            align="center",
                        ),
                        href="/",
                        style={"textDecoration": "none"},
                    ),
                ],
            ),
            color="dark",
            dark=True,
        )

        layout = html.Div(
            [
                navbar,
            ]
        )

        return layout

    def register_callbacks(self, app):
        pass
