from dash import html, dash_table, dcc
import dash_bootstrap_components as dbc

layout = html.Div([
    dbc.Row([
        html.H3("2016"),
        html.H3("Graph"),
    ], className='m-5'),

    dbc.Row([
        html.H3("2012"),
        html.H3("Graph"),
    ], className='m-5'),

], style={'backgroundColor': '#E6E6FA',
          'position': 'fixed',
          'width': '100%',
          'height': '100%',
          'left': '0px',
          }
)
