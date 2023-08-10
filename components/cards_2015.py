import dash_bootstrap_components as dbc
from dash import html

sale = [
    dbc.CardHeader("-2012-"),
    dbc.CardBody(
        [
            html.H5("$100,000,000",
                    className="card-title", style={"color": "#BF00BF"}),
            html.P("Total Sales (USD)", className="card-text fw-bold")
        ]
    ),
]

inv = [
    dbc.CardHeader("-2012-"),
    dbc.CardBody(
        [
            html.H5("$100,000,000",
                    className="card-title", style={"color": "#BF00BF"}),
            html.P("Number of invoices", className="card-text fw-bold")
        ]
    ),
]

bottlesold = [
    dbc.CardHeader("-2012-"),
    dbc.CardBody(
        [
            html.H5("$100,000,000",
                    className="card-title", style={"color": "#BF00BF"}),
            html.P("Bottle Sold", className="card-text fw-bold")
        ]
    ),
]

volumesold = [
    dbc.CardHeader("-2012-"),
    dbc.CardBody(
        [
            html.H5("$100,000,000",
                    className="card-title", style={"color": "#BF00BF"}),
            html.P("Volume Sold (Gallons)", className="card-text fw-bold")
        ]
    ),
]

statebottlecost = [
    dbc.CardHeader("-2012-"),
    dbc.CardBody(
        [
            html.H5("$100,000,000",
                    className="card-title", style={"color": "#BF00BF"}),
            html.P("State Bottle Cost", className="card-text fw-bold")
        ]
    ),
]

statebottleretail = [
    dbc.CardHeader("-2012-"),
    dbc.CardBody(
        [
            html.H5("$100,000,000",
                    className="card-title", style={"color": "#BF00BF"}),
            html.P("State Bottle Retail", className="card-text fw-bold")
        ]
    ),
]
