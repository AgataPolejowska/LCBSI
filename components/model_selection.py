from dash import html
from dash import dcc

# choose model from dropdown menu


class ModelSelect:
    def __init__(self, model_list):
        self.model_list = model_list
        self.model = self.model_list[0]

    def get_model(self):
        return self.model

    def get_layout(self):
        return html.Div(
            [
                html.H6("Choose Model"),
                dcc.Dropdown(
                    id="model-select",
                    options=[
                        {"label": model, "value": model} for model in self.model_list
                    ],
                    value=self.model_list[0],
                    style={"width": "100%"},
                ),
            ]
        )
