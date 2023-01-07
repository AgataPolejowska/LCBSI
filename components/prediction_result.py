import dash_bootstrap_components as dbc
from dash import html


class PredictionResult:
    def __init__(self, model, image):
        self.model = model
        self.image = image
        self.prediction = "test"

    def get_layout(self):
        return html.Div(
            [
                html.H6("Classification results"),
            ],
            id="classification-result",
            className="mb-4 mt-2 py-4 pt-2",
        )
