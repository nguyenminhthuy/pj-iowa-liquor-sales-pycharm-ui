import dash_bootstrap_components as dbc
from dash import html, callback, Output, Input, dcc
import plotly.graph_objs as go

sale = [
    dbc.CardHeader(id="card_sale_title", className="text-center"),
    dbc.CardBody([
        dbc.Row(html.H5(id="card_total_sales", className="card-title text-center", style={"color": "#32CD32"}),),
        dbc.Row([
            dbc.Col([
                html.Span("Previous", className="text-center"),
                html.P("$10,000", className="text-center")
            ]),
            dbc.Col([
                html.Span("Different", className="text-center"),
                html.P("$10,000", className="text-center")
            ]),
        ])
    ])
]

cost_sales = [
    dbc.CardHeader(id="card_cost_title", className="text-center"),
    dbc.CardBody([
        dbc.Row(html.H5(id="card_total_cost", className="card-title text-center", style={"color": "#32CD32"}),),
        dbc.Row([
            dbc.Col([
                html.Span("Previous", className="text-center"),
                html.P("$10,000", className="text-center")
            ]),
            dbc.Col([
                html.Span("Different", className="text-center"),
                html.P("$10,000", className="text-center")
            ]),
        ])
    ])
]

gross_profit = [
    dbc.CardHeader(id="card_grossProfit_title", className="text-center"),
    dbc.CardBody([
        dbc.Row(html.H5(id="card_total_grossProfit", className="card-title text-center", style={"color": "#32CD32"}),),
        dbc.Row([
            dbc.Col([
                html.Span("Previous", className="text-center"),
                html.P("$10,000", className="text-center")
            ]),
            dbc.Col([
                html.Span("Different", className="text-center"),
                html.P("$10,000", className="text-center")
            ]),
        ])
    ])
]

inv = [
    dbc.CardHeader(id="card_inv_title", className="text-center"),
    dbc.CardBody([
        dbc.Row(html.H5(id="card_total_inv", className="card-title text-center", style={"color": "#32CD32"}),),
        dbc.Row([
            dbc.Col([
                html.Span("Previous", className="text-center"),
                html.P("$10,000", className="text-center")
            ]),
            dbc.Col([
                html.Span("Different", className="text-center"),
                html.P("$10,000", className="text-center")
            ]),
        ])
    ])
]

bottleSold = [
    dbc.CardHeader(id="card_bottle_title", className="text-center"),
    dbc.CardBody([
        dbc.Row(html.H5(id="card_total_bottle", className="card-title text-center", style={"color": "#32CD32"}),),
        dbc.Row([
            dbc.Col([
                html.Span("Previous", className="text-center"),
                html.P("$10,000", className="text-center")
            ]),
            dbc.Col([
                html.Span("Different", className="text-center"),
                html.P("$10,000", className="text-center")
            ]),
        ])
    ])
]

volumeSold = [
    dbc.CardHeader(id="card_volume_title", className="text-center"),
    dbc.CardBody([
        dbc.Row(html.H5(id="card_total_volume", className="card-title text-center", style={"color": "#32CD32"}),),
        dbc.Row([
            dbc.Col([
                html.Span("Previous", className="text-center"),
                html.P("$10,000", className="text-center")
            ]),
            dbc.Col([
                html.Span("Different", className="text-center"),
                html.P("$10,000", className="text-center")
            ]),
        ])
    ])
]

# -------------------------------------------------
fig = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[4, 1, 2])])
month_graph = ([
    html.Div([
        dcc.Graph(figure=fig)
    ])
])

dow_graph = ([
    html.Div([
        dcc.Graph(figure=fig)
    ])
])

m_dow_graph = ([
    html.Div([
        dcc.Graph(figure=fig)
    ])
])

# -------------------------------------------------
top_highestItem_graph = ([
    html.Div(dcc.Graph(figure=fig))
])

top_mostItem_graph = ([
    html.Div(dcc.Graph(figure=fig))
])

# -------------------------------------------------
top_highestCat_graph = ([
    html.Div(dcc.Graph(figure=fig))
])

top_mostCat_graph = ([
    html.Div(dcc.Graph(figure=fig))
])

# -------------------------------------------------
top_highestVendor_graph = ([
    html.Div(dcc.Graph(figure=fig))
])

top_mostVendor_graph = ([
    html.Div(dcc.Graph(figure=fig))
])

# -------------------------------------------------
top_highestStore_graph = ([
    html.Div(dcc.Graph(figure=fig))
])

top_mostStore_graph = ([
    html.Div(dcc.Graph(figure=fig))
])

# -------------------------------------------------
top_highestCity_graph = ([
    html.Div(dcc.Graph(figure=fig))
])

top_mostCity_graph = ([
    html.Div(dcc.Graph(figure=fig))
])

# -------------------------------------------------
@callback(
    Output('card_sale_title', 'children'), # sale
    Output('card_total_sales', 'children'),
    Output('card_cost_title', 'children'), # cost
    Output('card_total_cost', 'children'),
    Output('card_grossProfit_title', 'children'), # retail
    Output('card_total_grossProfit', 'children'),
    Output('card_inv_title', 'children'), # inv
    Output('card_total_inv', 'children'),
    Output('card_bottle_title', 'children'), # bottle sold
    Output('card_total_bottle', 'children'),
    Output('card_volume_title', 'children'), # volume sold
    Output('card_total_volume', 'children'),    
    Input('store_y', 'data'),
)
def selected_y(y_selected):
    global sale_title, total_sales, cost_title, total_cost, grossProfit_title, total_grossProfit, inv_title,\
        total_inv, bottle_title, total_bottle, volume_title, total_volume

    if y_selected is None:
        sale_title = f"SALES N/A"
        total_sales = "$0"
        cost_title = f"COST OF SALES N/A"
        total_cost = "$0"
        grossProfit_title = f"GROSS PROFIT N/A"
        total_grossProfit = "$0"
        inv_title = f"NO. OF INVOICES N/A"
        total_inv = "$0"
        bottle_title = f"BOTTLE SOLD N/A"
        total_bottle = "$0"
        volume_title = f"VOLUME SOLD N/A"
        total_volume = "$0"

    else:
        # 2012
        if y_selected == 1:
            sale_title = f"SALES 2012"
            total_sales = "$S00,000,000"
            cost_title = f"COST OF SALES 2012"
            total_cost = "$C00,000,000"
            grossProfit_title = f"GROSS PROFIT 2012"
            total_grossProfit = "$G00,000,000"
            inv_title = f"NO. OF INVOICES 2012"
            total_inv = "I00,000,000"
            bottle_title = f"BOTTLE SOLD 2012"
            total_bottle = "B00,000,000"
            volume_title = f"VOLUME SOLD 2012"
            total_volume = "V00,000,000"

        # 2013
        if y_selected == 2:
            sale_title = f"SALES 2013"
            total_sales = "$100,000,000"
            cost_title = f"COST OF SALES 2013"
            total_cost = "$100,000,000"
            grossProfit_title = f"GROSS PROFIT 2013"
            total_grossProfit = "$100,000,000"
            inv_title = f"NO. OF INVOICES 2013"
            total_inv = "$100,000,000"
            bottle_title = f"BOTTLE SOLD 2013"
            total_bottle = "$100,000,000"
            volume_title = f"VOLUME SOLD 2013"
            total_volume = "$100,000,000"

        # 2014
        if y_selected == 3:
            sale_title = f"SALES 2014"
            total_sales = "$100,000,000"
            cost_title = f"COST OF SALES 2014"
            total_cost = "$100,000,000"
            grossProfit_title = f"GROSS PROFIT 2014"
            total_grossProfit = "$100,000,000"
            inv_title = f"NO. OF INVOICES 2014"
            total_inv = "$100,000,000"
            bottle_title = f"BOTTLE SOLD 2014"
            total_bottle = "$100,000,000"
            volume_title = f"VOLUME SOLD 2014"
            total_volume = "$100,000,000"

        # 2015
        if y_selected == 4:
            sale_title = f"SALES 2015"
            total_sales = "$100,000,000"
            cost_title = f"COST OF SALES 2015"
            total_cost = "$100,000,000"
            grossProfit_title = f"GROSS PROFIT 2015"
            total_grossProfit = "$100,000,000"
            inv_title = f"NO. OF INVOICES 2015"
            total_inv = "$100,000,000"
            bottle_title = f"BOTTLE SOLD 2015"
            total_bottle = "$100,000,000"
            volume_title = f"VOLUME SOLD 2015"
            total_volume = "$100,000,000"

        # 2016
        if y_selected == 5:
            sale_title = f"SALES 2016"
            total_sales = "$100,000,000"
            cost_title = f"COST OF SALES 2016"
            total_cost = "$100,000,000"
            grossProfit_title = f"GROSS PROFIT 2016"
            total_grossProfit = "$100,000,000"
            inv_title = f"NO. OF INVOICES 2016"
            total_inv = "$100,000,000"
            bottle_title = f"BOTTLE SOLD 2016"
            total_bottle = "$100,000,000"
            volume_title = f"VOLUME SOLD 2016"
            total_volume = "$100,000,000"

        # 2017
        if y_selected == 6:
            sale_title = f"SALES 2017"
            total_sales = "$100,000,000"
            cost_title = f"COST OF SALES 2017"
            total_cost = "$100,000,000"
            grossProfit_title = f"GROSS PROFIT 2017"
            total_grossProfit = "$100,000,000"
            inv_title = f"NO. OF INVOICES 2017"
            total_inv = "$100,000,000"
            bottle_title = f"BOTTLE SOLD 2017"
            total_bottle = "$100,000,000"
            volume_title = f"VOLUME SOLD 2017"
            total_volume = "$100,000,000"

        # 2018
        if y_selected == 7:
            sale_title = f"SALES 2018"
            total_sales = "$100,000,000"
            cost_title = f"COST OF SALES 2018"
            total_cost = "$100,000,000"
            grossProfit_title = f"GROSS PROFIT 2018"
            total_grossProfit = "$100,000,000"
            inv_title = f"NO. OF INVOICES 2018"
            total_inv = "$100,000,000"
            bottle_title = f"BOTTLE SOLD 2018"
            total_bottle = "$100,000,000"
            volume_title = f"VOLUME SOLD 2018"
            total_volume = "$100,000,000"

        # 2019
        if y_selected == 8:
            sale_title = f"SALES 2019"
            total_sales = "$100,000,000"
            cost_title = f"COST OF SALES 2019"
            total_cost = "$100,000,000"
            grossProfit_title = f"GROSS PROFIT 2019"
            total_grossProfit = "$100,000,000"
            inv_title = f"NO. OF INVOICES 2019"
            total_inv = "$100,000,000"
            bottle_title = f"BOTTLE SOLD 2019"
            total_bottle = "$100,000,000"
            volume_title = f"VOLUME SOLD 2019"
            total_volume = "$100,000,000"

        # 2020
        if y_selected == 9:
            sale_title = f"SALES 2020"
            total_sales = "$100,000,000"
            cost_title = f"COST OF SALES 2020"
            total_cost = "$100,000,000"
            grossProfit_title = f"GROSS PROFIT 2020"
            total_grossProfit = "$100,000,000"
            inv_title = f"NO. OF INVOICES 2020"
            total_inv = "$100,000,000"
            bottle_title = f"BOTTLE SOLD 2020"
            total_bottle = "$100,000,000"
            volume_title = f"VOLUME SOLD 2020"
            total_volume = "$100,000,000"

        # 2021
        if y_selected == 10:
            sale_title = f"SALES 2021"
            total_sales = "$100,000,000"
            cost_title = f"COST OF SALES 2021"
            total_cost = "$100,000,000"
            grossProfit_title = f"GROSS PROFIT 2021"
            total_grossProfit = "$100,000,000"
            inv_title = f"NO. OF INVOICES 2021"
            total_inv = "$100,000,000"
            bottle_title = f"BOTTLE SOLD 2021"
            total_bottle = "$100,000,000"
            volume_title = f"VOLUME SOLD 2021"
            total_volume = "$100,000,000"

        # 2022
        if y_selected == 11:
            sale_title = f"SALES 2022"
            total_sales = "$100,000,000"
            cost_title = f"COST OF SALES 2022"
            total_cost = "$100,000,000"
            grossProfit_title = f"GROSS PROFIT 2022"
            total_grossProfit = "$100,000,000"
            inv_title = f"NO. OF INVOICES 2022"
            total_inv = "$100,000,000"
            bottle_title = f"BOTTLE SOLD 2022"
            total_bottle = "$100,000,000"
            volume_title = f"VOLUME SOLD 2022"
            total_volume = "$100,000,000"

    return sale_title, total_sales, cost_title, total_cost, grossProfit_title, total_grossProfit, inv_title,\
        total_inv, bottle_title, total_bottle, volume_title, total_volume
