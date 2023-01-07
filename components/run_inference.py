import dash_bootstrap_components as dbc
from dash import html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate


class RunInferenceButton:
    def __init__(self, model, image):
        self.model = model
        self.image = image

    def get_layout(self):
        return html.Div(
            [
                html.H6("Run Inference"),
                dbc.Button(
                    "Run Inference",
                    id="run-inference-button",
                    color="primary",
                    className="mb-4",
                    style={"width": "100%"},
                ),
            ],
            className="my-4",
        )

    def register_callbacks(self, app):
        @app.callback(
            Output("prediction-result", "children"),
            Input("run-inference-button", "n_clicks"),
            State("model-select", "value"),
            State("image-displayed", "src"),
        )
        def run_inference(n_clicks, model, image):
            if n_clicks is None:
                raise PreventUpdate
            else:
                pass
                # return PredictionResult(model, image).get_layout()
