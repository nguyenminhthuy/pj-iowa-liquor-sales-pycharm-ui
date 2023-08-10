import dash_bootstrap_components as dbc
from dash import html

left_jumbotron = dbc.Col(
    html.Div([
        html.H4("SALES/NUMBER OF INVOICES (2014)", className="display-7 text-center"),
        html.Hr(className="my-3"),
        dbc.Row([
            dbc.Col([
                html.P("Graph1")
            ])
        ]),
    ],
        className="p-5 text-black rounded-3 shadow mb-5",
        style=dict(backgroundColor="#FFEBCD")
    ), md=6
)

right_jumbotron = dbc.Col(
    html.Div([
        html.H4("OTHERS (2014)", className="display-7 text-center"),
        html.Hr(className="my-3"),
        dbc.Row([
            dbc.Col([
                html.P("Graph1")
            ])
        ])
    ],
        className="p-5 border rounded-3 shadow mb-5",
        style=dict(backgroundColor="#FFEBCD")
    ), md=6
)
