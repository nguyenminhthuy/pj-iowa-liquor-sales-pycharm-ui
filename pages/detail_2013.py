import dash_bootstrap_components as dbc
from dash import html, dcc
from components import jumbotron_2013

tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': '3px solid #BF00BF',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': 'white',
    'color': 'black',
}

layout = html.Div([
    dbc.Row([
        jumbotron_2013.left_jumbotron,
        jumbotron_2013.right_jumbotron],
        className="align-items-md-stretch m-3",
    ),
    dbc.Row([
        dcc.Tabs([
            dcc.Tab(label='SALE REPORT',
                    style=tab_style, selected_style=tab_selected_style,
                    children=[
                        dcc.Graph(
                            figure={
                                'data': [
                                    {'x': [1, 2, 3], 'y': [4, 1, 2],
                                     'type': 'bar', 'name': 'SF'},
                                    {'x': [1, 2, 3], 'y': [2, 4, 5],
                                     'type': 'bar', 'name': 'Montréal'},
                                ]
                            }
                        )
                    ]
                    ),

            dcc.Tab(label='QUANTITY REPORT',
                    style=tab_style, selected_style=tab_selected_style,
                    children=[
                        dcc.Graph(
                            figure={
                                'data': [
                                    {'x': [1, 2, 3], 'y': [1, 4, 1],
                                     'type': 'bar', 'name': 'SF'},
                                    {'x': [1, 2, 3], 'y': [1, 2, 3],
                                     'type': 'bar', 'name': 'Montréal'},
                                ]
                            }
                        )
                    ]
                    ),
        ])
    ], className="align-items-md-stretch m-5",
    ),
])
