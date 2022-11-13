from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html


class ImageDisplay:
    def __init__(self, image, title="Image", wait_time=0):
        self.image = image
        self.title = title
        self.wait_time = wait_time

    def get_layout(self):

        # upload field for image
        image_upload = dcc.Upload(
            id="image-upload",
            children=html.Div(["Drag and drop or click to select an image to upload."]),
            style={
                "height": "80px",
                "lineHeight": "80px",
                "borderWidth": "1px",
                "borderStyle": "dashed",
                "borderRadius": "5px",
                "textAlign": "center",
                "margin": "10px",
            },
            multiple=False,
        )

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
                html.H6("Upload image"),
                image_upload,
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
