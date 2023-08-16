import dash_bootstrap_components as dbc
from dash import html, callback, Output, Input

left_jumbotron = dbc.Col([
    html.Div([
        html.H4(id="left_jump_title", className="display-7 text-center"),
        html.Hr(className="my-3"),
        dbc.Row([
            dbc.Col([
                html.P("Graph1")
            ])
        ]),
    ], className="p-5 text-black rounded-3 shadow mb-5",
        style=dict(backgroundColor="#FFEBCD")
    )
], md=6
)

right_jumbotron = dbc.Col([
    html.Div([
        html.H4(id="right_jump_title", className="display-7 text-center"),
        html.Hr(className="my-3"),
        dbc.Row([
            dbc.Col([
                html.P("Graph1")
            ])
        ])
    ], className="p-5 border rounded-3 shadow mb-5",
        style=dict(backgroundColor="#FFEBCD")
    )
], md=6
)

@callback(
    Output('left_jump_title', 'children'),
    Output('right_jump_title', 'children'),
    Input('store_y', 'data'),
)
def selected_y(y_selected):
    global left_title, right_title

    if y_selected is None:
        left_title = f"SALES/NUMBER OF INVOICES (N/A)"
        right_title = f"OTHERS (N/A)"
    else:
        # 2012
        if y_selected == 1:
            left_title = f"SALES/NUMBER OF INVOICES (2012)"
            right_title = f"OTHERS (2012)"

        # 2013
        if y_selected == 2:
            left_title = f"SALES/NUMBER OF INVOICES (2013)"
            right_title = f"OTHERS (2013)"

        # 2014
        if y_selected == 3:
            left_title = f"SALES/NUMBER OF INVOICES (2014)"
            right_title = f"OTHERS (2014)"

        # 2015
        if y_selected == 4:
            left_title = f"SALES/NUMBER OF INVOICES (2015)"
            right_title = f"OTHERS (2015)"

        # 2016
        if y_selected == 5:
            left_title = f"SALES/NUMBER OF INVOICES (2016)"
            right_title = f"OTHERS (2016)"

        # 2017
        if y_selected == 6:
            left_title = f"SALES/NUMBER OF INVOICES (2017)"
            right_title = f"OTHERS (2017)"

        # 2018
        if y_selected == 7:
            left_title = f"SALES/NUMBER OF INVOICES (2018)"
            right_title = f"OTHERS (2018)"

        # 2019
        if y_selected == 8:
            left_title = f"SALES/NUMBER OF INVOICES (2019)"
            right_title = f"OTHERS (2019)"

        # 2020
        if y_selected == 9:
            left_title = f"SALES/NUMBER OF INVOICES (2020)"
            right_title = f"OTHERS (2020)"

        # 2021
        if y_selected == 10:
            left_title = f"SALES/NUMBER OF INVOICES (2021)"
            right_title = f"OTHERS (2021)"

        # 2022
        if y_selected == 11:
            left_title = f"SALES/NUMBER OF INVOICES (2022)"
            right_title = f"OTHERS (2022)"

    return left_title, right_title