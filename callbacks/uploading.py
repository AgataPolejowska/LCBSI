from dash.dependencies import Input, Output


def register_image_uploading_callbacks(app):
    @app.callback(
        Output("image-display", "src"),
        Output("image-display", "style"),
        [Input("image-upload", "contents")],
    )
    def update_image(contents):
        if contents is not None:
            return contents, {"width": "100%", "height": "auto"}
        else:
            return "assets\\images\\test_image.jpg", {"width": "100%", "height": "auto"}
