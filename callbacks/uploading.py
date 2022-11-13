from dash.dependencies import Input, Output


def register_image_uploading_callbacks(app):
    """Register callbacks for uploading images.

    Args:
        app (dash.Dash): The app to register the callbacks to.
    """

    @app.callback(
        Output("image-display", "src"),
        # adjust size
        Output("image-display", "style"),
        [Input("image-upload", "contents")],
    )
    def update_image(contents):
        if contents is not None:
            return contents, {"width": "100%", "height": "auto"}
            return contents
        else:
            return "assets\\images\\test_image.jpg", {"width": "100%", "height": "auto"}
