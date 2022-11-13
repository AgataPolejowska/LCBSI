from dash import html
import dash_bootstrap_components as dbc


class PredictionResult:
    def __init__(self, model, image):
        self.model = model
        self.image = image
        self.prediction = "test"

    def get_layout(self):
        return html.Div(
            [
                html.H6("Prediction Result"),
                dbc.Table(
                    [
                        html.Thead(
                            [
                                html.Tr(
                                    [
                                        html.Th("Class"),
                                        html.Th("Probability"),
                                    ]
                                )
                            ]
                        ),
                        html.Tbody(
                            [
                                html.Tr(
                                    [
                                        html.Td("Basophil"),
                                        html.Td("0.1"),
                                    ]
                                ),
                                html.Tr(
                                    [
                                        html.Td("Neutrophil"),
                                        html.Td("0.2"),
                                    ]
                                ),
                                html.Tr(
                                    [
                                        html.Td("Eosinophil"),
                                        html.Td("0.3"),
                                    ]
                                ),
                                html.Tr(
                                    [
                                        html.Td("Lymphocyte"),
                                        html.Td("0.4"),
                                    ]
                                ),
                            ],
                        ),
                    ],
                    className="table",
                    striped=True,
                    bordered=True,
                    style={"width": "100%"},
                ),
            ],
            className="my-4 py-4",
        )
