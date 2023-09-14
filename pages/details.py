import dash_bootstrap_components as dbc
from dash import html, dcc, callback, Output, Input

from components import cards

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
            html.H3("GENERAL INFORMATION", style={"color": "rgb(30 51 118)"}),
            html.Hr(style={"width": "100%", "border": "2px solid #d62728"}),
            dbc.Col(dbc.Card(cards.sale, color="success", outline=True, className="shadow")),
            dbc.Col(dbc.Card(cards.inv, color="success", outline=True, className="shadow")),
            dbc.Col(dbc.Card(cards.bottleSold, color="success", outline=True, className="shadow")),
            dbc.Col(dbc.Card(cards.volumeSold, color="success", outline=True, className="shadow")),
            dbc.Col(dbc.Card(cards.stateBottleCost, color="success", outline=True, className="shadow")),
            dbc.Col(dbc.Card(cards.stateBottleRetail, color="success", outline=True, className="shadow")),
        ], className="m-5",
    ),

    dbc.Row(
        [
            html.H3("OVERALL SALES PER MONTH AND DAY OF WEEK", style={"color": "rgb(30 51 118)"}),
            html.Hr(style={"width": "100%", "border": "2px solid #d62728"}),
            dbc.Col(cards.month_graph, className="text-center border-end m-3"),
            dbc.Col(cards.m_dow_graph, className="text-center border-end m-3"),
            dbc.Col(cards.dow_graph, className="text-center border-end m-3"),
        ], className="m-4",
    ),

    dbc.Row(
        [
            html.H3("TOP GROSSING ITEMS", style={"color": "rgb(30 51 118)"}),
            html.Hr(style={"width": "100%", "border": "2px solid #d62728"}),
            dbc.Col(cards.top_highestItem_graph, className="text-center border-end m-3"),
            dbc.Col(cards.top_lowestItems_graph, className="text-center border-end m-3"),
        ], className="m-4",
    ),

    dbc.Row(
        [
            html.H3("TOP POPULAR ITEMS", style={"color": "rgb(30 51 118)"}),
            html.Hr(style={"width": "100%", "border": "2px solid #d62728"}),
            dbc.Col(cards.top_mostItem_graph, className="text-center border-end m-3"),
            dbc.Col(cards.top_leastItem_graph, className="text-center border-end m-3"),
        ], className="m-4",
    ),

    dbc.Row(
        [
            html.H3("TOP GROSSING CATEGORIES", style={"color": "rgb(30 51 118)"}),
            html.Hr(style={"width": "100%", "border": "2px solid #d62728"}),
            dbc.Col(cards.top_highestCat_graph, className="text-center border-end m-3"),
            dbc.Col(cards.top_lowestCat_graph, className="text-center border-end m-3"),
        ], className="m-4",
    ),

    dbc.Row(
        [
            html.H3("TOP POPULAR CATEGORIES", style={"color": "rgb(30 51 118)"}),
            html.Hr(style={"width": "100%", "border": "2px solid #d62728"}),
            dbc.Col(cards.top_mostCat_graph, className="text-center border-end m-3"),
            dbc.Col(cards.top_leastCat_graph, className="text-center border-end m-3"),
        ], className="m-4",
    ),

dbc.Row(
        [
            html.H3("TOP GROSSING VENDORS", style={"color": "rgb(30 51 118)"}),
            html.Hr(style={"width": "100%", "border": "2px solid #d62728"}),
            dbc.Col(cards.top_highestVendor_graph, className="text-center border-end m-3"),
            dbc.Col(cards.top_lowestVendor_graph, className="text-center border-end m-3"),
        ], className="m-4",
    ),

    dbc.Row(
        [
            html.H3("TOP POPULAR VENDORS", style={"color": "rgb(30 51 118)"}),
            html.Hr(style={"width": "100%", "border": "2px solid #d62728"}),
            dbc.Col(cards.top_mostVendor_graph, className="text-center border-end m-3"),
            dbc.Col(cards.top_leastVendor_graph, className="text-center border-end m-3"),
        ], className="m-4",
    ),

    dbc.Row(
        [
            html.H3("TOP GROSSING STORE", style={"color": "rgb(30 51 118)"}),
            html.Hr(style={"width": "100%", "border": "2px solid #d62728"}),
            dbc.Col(cards.top_highestStore_graph, className="text-center border-end m-3"),
            dbc.Col(cards.top_lowestStore_graph, className="text-center border-end m-3"),
        ], className="m-4",
    ),

    dbc.Row(
        [
            html.H3("TOP POPULAR STORE", style={"color": "rgb(30 51 118)"}),
            html.Hr(style={"width": "100%", "border": "2px solid #d62728"}),
            dbc.Col(cards.top_mostStore_graph, className="text-center border-end m-3"),
            dbc.Col(cards.top_leastStore_graph, className="text-center border-end m-3"),
        ], className="m-4",
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
