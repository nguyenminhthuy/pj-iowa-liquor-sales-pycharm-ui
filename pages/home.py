import dash_bootstrap_components as dbc
from dash import html
from components import cards

layout = html.Div([
    dbc.Row(
        [
            dbc.Col([
                dbc.Row([
                    html.H5("SALES HISTORICAL TREND 2012-2022"),
                    dbc.Col(cards.month_graph, className="text-center m-3")
                ], className="text-center m-4"),
                dbc.Row(
                    html.H5("TABLE"),
                    className="text-center m-4"),
            ]),

            dbc.Col([
                dbc.Row([
                    html.H5("COST AND GROSS PROFIT HISTORICAL TREND 2012-2022"),
                    dbc.Col(cards.month_graph, className="text-center m-3")
                ], className="text-center m-4"),
                dbc.Row(
                    html.H5("TABLE"),
                    className="text-center border-end m-4"),
            ]),
        ], className="m-4",
    ),
])
