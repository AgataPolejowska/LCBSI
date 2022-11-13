import dash
import dash_bootstrap_components as dbc


from components import (
    image_display,
    model_selection,
    prediction_result,
    run_inference,
)


dash.register_page(__name__)


image_displayed = image_display.ImageDisplay(
    image="assets\\images\\test_image.jpg",
    title="Test image",
    wait_time=0,
)

model_list = ["ResNet", "ViT"]
model_selection = model_selection.ModelSelect(model_list)
prediction_result = prediction_result.PredictionResult(
    model_selection.model, image_displayed.image
)
run_inference_button = run_inference.RunInferenceButton(
    model_selection.model, image_displayed.image
)

layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col([image_displayed.get_layout()], className="p-4 col-6"),
                # add prediction column with choosing model
                dbc.Col(
                    [
                        model_selection.get_layout(),
                        run_inference_button.get_layout(),
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
