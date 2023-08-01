import dash_bootstrap_components as dbc
from PIL import Image
from dash import html
from components import canvas
# Header
header = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        html.Img(
                            id="logo",
                            src=Image.open("img/logo.png"),
                            height="60px",
                        ),
                        md="auto",
                    ),
                    dbc.Col(
                        [
                            html.Div(
                                [
                                    html.H3("IOWA LIQUOR SALES"),
                                    html.P("Based on sales 2012-2022"),
                                ],
                                id="app-title",
                            )
                        ],
                        md=True,
                        align="center",
                    ),
                ],
                align="center",
            ),
            dbc.Row([
                dbc.Col(canvas.off_canvas)
            ], align="center"),
        ], className='m-2',
        fluid=True,
    ),
    # dark=True,
    color="rgb(30 51 118)",
    sticky="top",
)
