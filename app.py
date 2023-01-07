import dash
from dash import dcc, html
from flask import Flask
from transformers import pipeline

from components import navbar
from constants import EXTERNAL_STYLESHEETS

nav = navbar.Navbar()

server = Flask(__name__)


def get_layout():
    layout = html.Div(
        [
            dcc.Location(id="url", refresh=False),
            nav.get_layout(),
            html.Div(id="page-content", children=[], className="container-fluid"),
        ]
    )
    return layout


app = dash.Dash(
    __name__,
    server=server,
    external_stylesheets=EXTERNAL_STYLESHEETS,
    title="LCBSI",
    suppress_callback_exceptions=True,
)

app.title = "LCBSI"
app._favicon = "assets\\favicon\\favicon.ico"

# Base app layout
app.layout = get_layout
