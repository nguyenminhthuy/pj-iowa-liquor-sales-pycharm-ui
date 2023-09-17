import dash_bootstrap_components as dbc
import pandas as pd
from dash import Dash, dash_table, dcc, html, Input, Output, callback
import plotly.express as px
from components import cards

table_header = [
    html.Thead(html.Tr([html.Th("First Name"), html.Th("Last Name")]))
]

row1 = html.Tr([html.Td("Arthur"), html.Td("Dent")])
row2 = html.Tr([html.Td("Ford"), html.Td("Prefect")])
row3 = html.Tr([html.Td("Zaphod"), html.Td("Beeblebrox")])
row4 = html.Tr([html.Td("Trillian"), html.Td("Astra")])
table_body = [html.Tbody([row1, row2, row3, row4])]
table = dbc.Table(table_header + table_body, bordered=True)

layout = html.Div([
    dbc.Row(
        [
            html.H3("SALES PERFORMANCE DASHBOARD", style={"color": "rgb(30 51 118)"}),
            html.Hr(style={"width": "100%", "border": "2px solid #d62728"}),
            dbc.Col([
                dbc.Row([
                    html.H5("SALES HISTORICAL TREND 2012-2022"),
                    dbc.Col(cards.month_graph, className="text-center m-3")
                ], className="text-center m-4"),
                dbc.Row(
                    table,
                    className="text-center m-4"),
            ]),

            dbc.Col([
                dbc.Row([
                    html.H5("GROSS PROFIT HISTORICAL TREND 2012-2022"),
                    dbc.Col(cards.month_graph, className="text-center m-3")
                ], className="text-center m-4"),
                dbc.Row(
                    table,
                    className="text-center border-end m-4"),
            ]),
        ], className="m-4",
    ),
])
