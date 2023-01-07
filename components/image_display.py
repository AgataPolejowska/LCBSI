import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output


class ImageDisplay:
    def __init__(self, image, title="Image", wait_time=0):
        self.image = image
        self.title = title
        self.wait_time = wait_time

    def get_layout(self):
        image_display = html.Img(
            id="image-display",
            src=self.image,
            style={"width": "100%", "height": "auto"},
        )

        image_display_card = dbc.Card(
            [
                dbc.CardHeader(self.title),
                dbc.CardBody(
                    [
                        image_display,
                    ],
                    className="p-0",
                ),
            ],
            className="h-100",
            style={"margin": "10px"},
        )

        layout = html.Div(
            [
                image_display_card,
                dcc.Interval(id="interval", interval=self.wait_time * 1000),
            ]
        )
        return layout

    def register_callbacks(self, app):
        @app.callback(
            Output("image-display", "src"),
            [Input("interval", "n_intervals")],
        )
        def update_image(n):
            return self.image
