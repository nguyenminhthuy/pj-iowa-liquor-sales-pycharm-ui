import dash_bootstrap_components as dbc
from dash import html, callback, Output, Input

sale = [
    dbc.CardHeader(id="card_sale_title"),
    dbc.CardBody(
        [
            html.H5(id="card_total_sales",
                    className="card-title", style={"color": "#BF00BF"}),
            html.P("Total Sales (USD)", className="card-text fw-bold")
        ]
    ),
]

inv = [
    dbc.CardHeader(id="card_inv_title"),
    dbc.CardBody(
        [
            html.H5(id="card_total_inv",
                    className="card-title", style={"color": "#BF00BF"}),
            html.P("Number of invoices", className="card-text fw-bold")
        ]
    ),
]

bottlesold = [
    dbc.CardHeader(id="card_bottle_title"),
    dbc.CardBody(
        [
            html.H5(id="card_total_bottle",
                    className="card-title", style={"color": "#BF00BF"}),
            html.P("Bottle Sold", className="card-text fw-bold")
        ]
    ),
]

volumesold = [
    dbc.CardHeader(id="card_volume_title"),
    dbc.CardBody(
        [
            html.H5(id="card_total_volume",
                    className="card-title", style={"color": "#BF00BF"}),
            html.P("Volume Sold (Gallons)", className="card-text fw-bold")
        ]
    ),
]

statebottlecost = [
    dbc.CardHeader(id="card_cost_title"),
    dbc.CardBody(
        [
            html.H5(id="card_total_cost",
                    className="card-title", style={"color": "#BF00BF"}),
            html.P("State Bottle Cost", className="card-text fw-bold")
        ]
    ),
]

statebottleretail = [
    dbc.CardHeader(id="card_retail_title"),
    dbc.CardBody(
        [
            html.H5(id="card_total_retail",
                    className="card-title", style={"color": "#BF00BF"}),
            html.P("State Bottle Retail", className="card-text fw-bold")
        ]
    ),
]

# -------------------------------------------------
@callback(
    Output('card_sale_title', 'children'), # sale
    Output('card_total_sales', 'children'),
    Output('card_inv_title', 'children'), # inv
    Output('card_total_inv', 'children'),
    Output('card_bottle_title', 'children'), # bottle sold
    Output('card_total_bottle', 'children'),
    Output('card_volume_title', 'children'), # volume sold
    Output('card_total_volume', 'children'),
    Output('card_cost_title', 'children'), # cost
    Output('card_total_cost', 'children'),
    Output('card_retail_title', 'children'), # retail
    Output('card_total_retail', 'children'),
    Input('store_y', 'data'),
)
def selected_y(y_selected):
    global sale_title, total_sales, inv_title, total_inv, bottle_title, total_bottle, volume_title, \
        total_volume, cost_title, total_cost, retail_title, total_retail

    if y_selected is None:
        sale_title = f"Year: N/A"
        total_sales = "$0"
        inv_title = f"Year: N/A"
        total_inv = "$0"
        bottle_title = f"Year: N/A"
        total_bottle = "$0"
        volume_title = f"Year: N/A"
        total_volume = "$0"
        cost_title = f"Year: N/A"
        total_cost = "$0"
        retail_title = f"Year: N/A"
        total_retail = "$0"
    else:
        # 2012
        if y_selected == 1:
            sale_title = f"Year: 2012"
            total_sales = "$100,000,000"
            inv_title = f"Year: 2012"
            total_inv = "$100,000,000"
            bottle_title = f"Year: 2012"
            total_bottle = "$100,000,000"
            volume_title = f"Year: 2012"
            total_volume = "$100,000,000"
            cost_title = f"Year: 2012"
            total_cost = "$100,000,000"
            retail_title = f"Year: 2012"
            total_retail = "$100,000,000"

        # 2013
        if y_selected == 2:
            sale_title = f"Year: 2013"
            total_sales = "$100,000,000"
            inv_title = f"Year: 2013"
            total_inv = "$100,000,000"
            bottle_title = f"Year: 2013"
            total_bottle = "$100,000,000"
            volume_title = f"Year: 2013"
            total_volume = "$100,000,000"
            cost_title = f"Year: 2013"
            total_cost = "$100,000,000"
            retail_title = f"Year: 2013"
            total_retail = "$100,000,000"

        # 2014
        if y_selected == 3:
            sale_title = f"Year: 2014"
            total_sales = "$100,000,000"
            inv_title = f"Year: 2014"
            total_inv = "$100,000,000"
            bottle_title = f"Year: 2014"
            total_bottle = "$100,000,000"
            volume_title = f"Year: 2014"
            total_volume = "$100,000,000"
            cost_title = f"Year: 2014"
            total_cost = "$100,000,000"
            retail_title = f"Year: 2014"
            total_retail = "$100,000,000"

        # 2015
        if y_selected == 4:
            sale_title = f"Year: 2015"
            total_sales = "$100,000,000"
            inv_title = f"Year: 2015"
            total_inv = "$100,000,000"
            bottle_title = f"Year: 2015"
            total_bottle = "$100,000,000"
            volume_title = f"Year: 2015"
            total_volume = "$100,000,000"
            cost_title = f"Year: 2015"
            total_cost = "$100,000,000"
            retail_title = f"Year: 2015"
            total_retail = "$100,000,000"

        # 2016
        if y_selected == 5:
            sale_title = f"Year: 2016"
            total_sales = "$100,000,000"
            inv_title = f"Year: 2016"
            total_inv = "$100,000,000"
            bottle_title = f"Year: 2016"
            total_bottle = "$100,000,000"
            volume_title = f"Year: 2016"
            total_volume = "$100,000,000"
            cost_title = f"Year: 2016"
            total_cost = "$100,000,000"
            retail_title = f"Year: 2016"
            total_retail = "$100,000,000"

        # 2017
        if y_selected == 6:
            sale_title = f"Year: 2017"
            total_sales = "$100,000,000"
            inv_title = f"Year: 2017"
            total_inv = "$100,000,000"
            bottle_title = f"Year: 2017"
            total_bottle = "$100,000,000"
            volume_title = f"Year: 2017"
            total_volume = "$100,000,000"
            cost_title = f"Year: 2017"
            total_cost = "$100,000,000"
            retail_title = f"Year: 2017"
            total_retail = "$100,000,000"

        # 2018
        if y_selected == 7:
            sale_title = f"Year: 2018"
            total_sales = "$100,000,000"
            inv_title = f"Year: 2018"
            total_inv = "$100,000,000"
            bottle_title = f"Year: 2018"
            total_bottle = "$100,000,000"
            volume_title = f"Year: 2018"
            total_volume = "$100,000,000"
            cost_title = f"Year: 2018"
            total_cost = "$100,000,000"
            retail_title = f"Year: 2018"
            total_retail = "$100,000,000"

        # 2019
        if y_selected == 8:
            sale_title = f"Year: 2019"
            total_sales = "$100,000,000"
            inv_title = f"Year: 2019"
            total_inv = "$100,000,000"
            bottle_title = f"Year: 2019"
            total_bottle = "$100,000,000"
            volume_title = f"Year: 2019"
            total_volume = "$100,000,000"
            cost_title = f"Year: 2019"
            total_cost = "$100,000,000"
            retail_title = f"Year: 2019"
            total_retail = "$100,000,000"

        # 2020
        if y_selected == 9:
            sale_title = f"Year: 2020"
            total_sales = "$100,000,000"
            inv_title = f"Year: 2020"
            total_inv = "$100,000,000"
            bottle_title = f"Year: 2020"
            total_bottle = "$100,000,000"
            volume_title = f"Year: 2020"
            total_volume = "$100,000,000"
            cost_title = f"Year: 2020"
            total_cost = "$100,000,000"
            retail_title = f"Year: 2020"
            total_retail = "$100,000,000"

        # 2021
        if y_selected == 10:
            sale_title = f"Year: 2021"
            total_sales = "$100,000,000"
            inv_title = f"Year: 2021"
            total_inv = "$100,000,000"
            bottle_title = f"Year: 2021"
            total_bottle = "$100,000,000"
            volume_title = f"Year: 2021"
            total_volume = "$100,000,000"
            cost_title = f"Year: 2021"
            total_cost = "$100,000,000"
            retail_title = f"Year: 2021"
            total_retail = "$100,000,000"

        # 2022
        if y_selected == 11:
            sale_title = f"Year: 2022"
            total_sales = "$100,000,000"
            inv_title = f"Year: 2022"
            total_inv = "$100,000,000"
            bottle_title = f"Year: 2022"
            total_bottle = "$100,000,000"
            volume_title = f"Year: 2022"
            total_volume = "$100,000,000"
            cost_title = f"Year: 2022"
            total_cost = "$100,000,000"
            retail_title = f"Year: 2022"
            total_retail = "$100,000,000"

    return sale_title, total_sales, inv_title, total_inv, bottle_title, total_bottle, volume_title, \
        total_volume, cost_title, total_cost, retail_title, total_retail
