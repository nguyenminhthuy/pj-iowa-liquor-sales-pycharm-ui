from dash import html, dash_table, dcc
import dash_bootstrap_components as dbc

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

], style={'backgroundColor': '#FFE4E1',
          'position': 'fixed',
          'width': '100%',
          'height': '100%',
          'left': '0px',
          }
)
