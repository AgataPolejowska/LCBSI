import dash
import dash_bootstrap_components as dbc
from dash import html
from dash import dcc

from components import (image_display, model_selection, prediction_result)

dash.register_page(__name__)

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

image_displayed = image_display.ImageDisplay(
    image="assets\\images\\test_image.jpg",
    title="Image",
    wait_time=0,
)

model_list = ["ViT-swin", "ViT-base"]
model_selection = model_selection.ModelSelect(model_list)
prediction_result = prediction_result.PredictionResult(
    model_selection.model, image_displayed.image
)

layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col([image_displayed.get_layout()], className="p-4 col-6"),
                dbc.Col(
                    [
                        html.Div([
                            html.H6("Upload image"),
                            image_upload,
                        ],
                        className="my-4 mt-5"
                        ),
                        model_selection.get_layout(),
                        html.Div(
                            [
                                html.H6("Classify"),
                                dbc.Button(
                                    "Run classification",
                                    id="classify-button",
                                    color="primary",
                                    className="mb-4",
                                    style={"width": "100%"},
                                ),
                            ],
                            className="my-4 mb-2",
                        ),
                        prediction_result.get_layout(),
                    ],
                    className="p-4 col-6",
                ),
            ],
            className="h-100",
        ),
    ],
    fluid=True,
    className="m-0 bg-light",
)
