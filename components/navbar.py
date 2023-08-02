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
                dbc.Col(
                    dbc.Button(children=[html.I(className="fa fa-home fa-lg")],
                               href="/",
                               style=dict(fontSize="20px",
                                          backgroundColor="rgb(237, 201, 72)",
                                          textAlign="center",
                                          color="black", border="none")
                               ), md="auto",
                ),
                dbc.Col(
                    dbc.DropdownMenu(
                        [dbc.DropdownMenuItem("2012", href="/detail-2012"),
                         dbc.DropdownMenuItem("2013", href="/detail-2013"),
                         dbc.DropdownMenuItem("2014", href="/detail-2014"),
                         dbc.DropdownMenuItem("2015", href="/detail-2015"),
                         dbc.DropdownMenuItem("2016", href="/detail-2016"),
                         dbc.DropdownMenuItem("2017", href="/detail-2017"),
                         dbc.DropdownMenuItem("2018", href="/detail-2018"),
                         dbc.DropdownMenuItem("2019", href="/detail-2019"),
                         dbc.DropdownMenuItem("2020", href="/detail-2020"),
                         dbc.DropdownMenuItem("2021", href="/detail-2021"),
                         dbc.DropdownMenuItem("2022", href="/detail-2022")],
                        label=[html.I(className="fa fa-calendar-minus-o fa-lg"), " Select a year of sales"],
                        color="primary", className="m-1", size="lg",
                        toggle_style={
                            'background': 'rgb(237, 201, 72)',
                            'color': 'black', 'border': '0px'
                        },
                    ),
                    md="auto",
                ),
                dbc.Col(canvas.off_canvas, md="auto", )
            ], align="center"),
        ], className='m-2',
        fluid=True,
    ),
    # dark=True,
    color="rgb(30 51 118)",
    sticky="top",
)
