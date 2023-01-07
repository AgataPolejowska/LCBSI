from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
from transformers import pipeline
from PIL import Image
from io import BytesIO
import base64
import re
import pandas as pd


def register_predicting_callbacks(app):
    @app.callback(
        Output("classification-result", "children"),
        Input("classify-button", "n_clicks"),
        State("model-select", "value"),
        State("image-display", "src"),
    )
    def run_inference(n_clicks, model, image):
        if n_clicks is None:
            raise PreventUpdate
        else:
            model_hf = {
                "ViT-swin": "polejowska/swin-tiny-patch4-window7-224-lcbsi-wbc",
                "ViT-base": "polejowska/vit-base-patch16-224-in21k-lcbsi",
            }
            
            image_data = re.sub('^data:image/.+;base64,', '', image)
            image = Image.open(BytesIO(base64.b64decode(image_data)))

            pipe = pipeline("image-classification", model_hf[model])

            results = pipe(image)
            results_df = pd.DataFrame.from_dict(results)
            results_df["score"] = results_df["score"].apply(lambda x: round(x * 100, 2))
            results_df["score"] = results_df["score"].astype(str) + "%"
            results_table = dbc.Table.from_dataframe(results_df, striped=True, bordered=True, hover=True)

            return results_table
