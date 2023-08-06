import dash_bootstrap_components as dbc
from dash import html

layout = html.Div([
    dbc.Row([
        html.H3("OVERALL SALES AND INVOICES DATA YEAR OVER YEAR GROWTH"),
        html.H3("Graph"),
    ], className='m-5'),

    dbc.Row([
        html.H3("OVERALL SALES AND INVOICES DATA YEAR OVER YEAR GROWTH"),
        html.H3("table"),
    ], className='m-5'),

    dbc.Row([
        html.H3("OVERALL SALES AND INVOICES DATA YEAR OVER YEAR GROWTH"),
        html.H3("Graph"),
    ], className='m-5'),

])
