import dash_bootstrap_components as dbc
from dash import html

left_jumbotron = dbc.Col(
    html.Div([
        html.H4("SALES/NUMBER OF INVOICES (2012)", className="display-7"),
        html.Hr(className="my-3"),
        dbc.Row([
            dbc.Col([
                html.H3("$100,000,000",
                        style={"color": "#BF00BF"}),
                html.P("SALES (USD)", className="fw-bold"),
            ], md=4),

            dbc.Col([
                html.P("Graph1")
            ], md=8)
        ]),
        html.Hr(className="my-3"),
        dbc.Row([
            dbc.Col([
                html.H3("1,000,000",
                        style={"color": "#BF00BF"}),
                html.P("INVOICES", className="fw-bold"),
            ], md=4),

            dbc.Col([
                html.P("Graph1")
            ], md=8)
        ]),
    ],
        className="p-5 text-black rounded-3 shadow mb-5",
        style=dict(backgroundColor="#FFEBCD")
    ), md=6
)

right_jumbotron = dbc.Col(
    html.Div([
        html.H4("OTHERS (2012)", className="display-7"),
        html.Hr(className="my-3"),
        dbc.Row([
            dbc.Col([
                dbc.Row([
                    html.H3("1,000,000",
                            style={"color": "#BF00BF"}),
                    html.P("BOTTLE SOLD", className="fw-bold")
                ]),
                dbc.Row([
                    html.H3("1,000,000",
                            style={"color": "#BF00BF"}),
                    html.P("VOLUME SOLD (GALLONS)", className="fw-bold")
                ]),
            ], md=4),

            dbc.Col([
                html.P("Graph1")
            ], md=8)
        ]),
        html.Hr(className="my-3"),
        dbc.Row([
            dbc.Col([
                dbc.Row([
                    html.H3("1,000,000",
                            style={"color": "#BF00BF"}),
                    html.P("STATE BOTTLE COST", className="fw-bold")
                ]),
                dbc.Row([
                    html.H3("$10,000,000",
                            style={"color": "#BF00BF"}),
                    html.P("STATE BOTTLE RETAIL", className="fw-bold")
                ]),
            ], md=4),

            dbc.Col([
                html.P("Graph1")
            ], md=8)
        ]),
    ],
        className="p-5 border rounded-3 shadow mb-5",
        style=dict(backgroundColor="#FFEBCD")
    ), md=6
)
