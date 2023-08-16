import dash_bootstrap_components as dbc
from dash import html, dcc, callback, Output, Input, State, ALL
from components import jumbotron, cards

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
    dbc.Row(
        [
            dbc.Col(dbc.Card(cards.sale,
                             color="success", outline=True, className="shadow")),
            dbc.Col(dbc.Card(cards.inv,
                             color="success", outline=True, className="shadow")),
            dbc.Col(dbc.Card(cards.bottlesold,
                             color="success", outline=True, className="shadow")),
            dbc.Col(dbc.Card(cards.volumesold,
                             color="success", outline=True, className="shadow")),
            dbc.Col(dbc.Card(cards.statebottlecost,
                             color="success", outline=True, className="shadow")),
            dbc.Col(dbc.Card(cards.statebottleretail,
                             color="success", outline=True, className="shadow")),
        ], className="m-4",
    ),

    dbc.Row([
        jumbotron.left_jumbotron,
        jumbotron.right_jumbotron],
        className="align-items-md-stretch m-3",
    ),

    dbc.Row([
        dcc.Tabs([
            dcc.Tab(id="left_tab_title", style=tab_style, selected_style=tab_selected_style,
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
                    ]),

            dcc.Tab(id="right_tab_title", style=tab_style, selected_style=tab_selected_style,
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
                    ]),
        ])
    ], className="align-items-md-stretch m-5",
    ),
])

@callback(
    Output('left_tab_title', 'label'),
    Output('right_tab_title', 'label'),
    Input('store_y', 'data'),
)
def selected_y(y_selected):
    global left_title, right_title

    if y_selected is None:
        left_title = f"SALE REPORT (N/A)"
        right_title = f"QUANTITY REPORT (N/A)"
    else:
        # 2012
        if y_selected == 1:
            left_title = f"SALE REPORT (2012)"
            right_title = f"QUANTITY REPORT (2012)"

        # 2013
        if y_selected == 2:
            left_title = f"SALE REPORT (2013)"
            right_title = f"QUANTITY REPORT (2013)"

        # 2014
        if y_selected == 3:
            left_title = f"SALE REPORT (2014)"
            right_title = f"QUANTITY REPORT (2014)"

        # 2015
        if y_selected == 4:
            left_title = f"SALE REPORT (2015)"
            right_title = f"QUANTITY REPORT (2015)"

        # 2016
        if y_selected == 5:
            left_title = f"SALE REPORT (2016)"
            right_title = f"QUANTITY REPORT (2016)"

        # 2017
        if y_selected == 6:
            left_title = f"SALE REPORT (2017)"
            right_title = f"QUANTITY REPORT (2017)"

        # 2018
        if y_selected == 7:
            left_title = f"SALE REPORT (2018)"
            right_title = f"QUANTITY REPORT (2018)"

        # 2019
        if y_selected == 8:
            left_title = f"SALE REPORT (2019)"
            right_title = f"QUANTITY REPORT (2019)"

        # 2020
        if y_selected == 9:
            left_title = f"SALE REPORT (2020)"
            right_title = f"QUANTITY REPORT (2020)"

        # 2021
        if y_selected == 10:
            left_title = f"SALE REPORT (2021)"
            right_title = f"QUANTITY REPORT (2021)"

        # 2022
        if y_selected == 11:
            left_title = f"SALE REPORT (2022)"
            right_title = f"QUANTITY REPORT (2022)"

    return left_title, right_title