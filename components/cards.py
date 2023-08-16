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
    Output('card_sale_title', 'children'),
    Output('card_total_sales', 'children'),
    Input('store_y', 'data'),
)
def selected_y(y_selected):
    global title, total_sales

    if y_selected is None:
        title = f"Year: N/A"
        total_sales = "$0"
    else:
        # 2012
        if y_selected == 1:
            title = f"Year: 2012"
            total_sales = "$100,000,000"

        # 2013
        if y_selected == 2:
            title = f"Year: 2013"
            total_sales = "$100,000,000"

        # 2014
        if y_selected == 3:
            title = f"Year: 2014"
            total_sales = "$100,000,000"

        # 2015
        if y_selected == 4:
            title = f"Year: 2015"
            total_sales = "$100,000,000"

        # 2016
        if y_selected == 5:
            title = f"Year: 2016"
            total_sales = "$100,000,000"

        # 2017
        if y_selected == 6:
            title = f"Year: 2017"
            total_sales = "$100,000,000"

        # 2018
        if y_selected == 7:
            title = f"Year: 2018"
            total_sales = "$100,000,000"

        # 2019
        if y_selected == 8:
            title = f"Year: 2019"
            total_sales = "$100,000,000"

        # 2020
        if y_selected == 9:
            title = f"Year: 2020"
            total_sales = "$100,000,000"

        # 2021
        if y_selected == 10:
            title = f"Year: 2021"
            total_sales = "$100,000,000"

        # 2022
        if y_selected == 11:
            title = f"Year: 2022"
            total_sales = "$100,000,000"

    return title, total_sales

# -------------------------------------------------
@callback(
    Output('card_inv_title', 'children'),
    Output('card_total_inv', 'children'),
    Input('store_y', 'data'),
)
def selected_y(y_selected):
    global title, total_sales

    if y_selected is None:
        title = f"Year: N/A"
        total_sales = "$0"
    else:
        # 2012
        if y_selected == 1:
            title = f"Year: 2012"
            total_sales = "$100,000,000"

        # 2013
        if y_selected == 2:
            title = f"Year: 2013"
            total_sales = "$100,000,000"

        # 2014
        if y_selected == 3:
            title = f"Year: 2014"
            total_sales = "$100,000,000"

        # 2015
        if y_selected == 4:
            title = f"Year: 2015"
            total_sales = "$100,000,000"

        # 2016
        if y_selected == 5:
            title = f"Year: 2016"
            total_sales = "$100,000,000"

        # 2017
        if y_selected == 6:
            title = f"Year: 2017"
            total_sales = "$100,000,000"

        # 2018
        if y_selected == 7:
            title = f"Year: 2018"
            total_sales = "$100,000,000"

        # 2019
        if y_selected == 8:
            title = f"Year: 2019"
            total_sales = "$100,000,000"

        # 2020
        if y_selected == 9:
            title = f"Year: 2020"
            total_sales = "$100,000,000"

        # 2021
        if y_selected == 10:
            title = f"Year: 2021"
            total_sales = "$100,000,000"

        # 2022
        if y_selected == 11:
            title = f"Year: 2022"
            total_sales = "$100,000,000"

    return title, total_sales

# -------------------------------------------------
@callback(
    Output('card_bottle_title', 'children'),
    Output('card_total_bottle', 'children'),
    Input('store_y', 'data'),
)
def selected_y(y_selected):
    global title, total_sales

    if y_selected is None:
        title = f"Year: N/A"
        total_sales = "$0"
    else:
        # 2012
        if y_selected == 1:
            title = f"Year: 2012"
            total_sales = "$100,000,000"

        # 2013
        if y_selected == 2:
            title = f"Year: 2013"
            total_sales = "$100,000,000"

        # 2014
        if y_selected == 3:
            title = f"Year: 2014"
            total_sales = "$100,000,000"

        # 2015
        if y_selected == 4:
            title = f"Year: 2015"
            total_sales = "$100,000,000"

        # 2016
        if y_selected == 5:
            title = f"Year: 2016"
            total_sales = "$100,000,000"

        # 2017
        if y_selected == 6:
            title = f"Year: 2017"
            total_sales = "$100,000,000"

        # 2018
        if y_selected == 7:
            title = f"Year: 2018"
            total_sales = "$100,000,000"

        # 2019
        if y_selected == 8:
            title = f"Year: 2019"
            total_sales = "$100,000,000"

        # 2020
        if y_selected == 9:
            title = f"Year: 2020"
            total_sales = "$100,000,000"

        # 2021
        if y_selected == 10:
            title = f"Year: 2021"
            total_sales = "$100,000,000"

        # 2022
        if y_selected == 11:
            title = f"Year: 2022"
            total_sales = "$100,000,000"

    return title, total_sales

# -------------------------------------------------
@callback(
    Output('card_volume_title', 'children'),
    Output('card_total_volume', 'children'),
    Input('store_y', 'data'),
)
def selected_y(y_selected):
    global title, total_sales

    if y_selected is None:
        title = f"Year: N/A"
        total_sales = "$0"
    else:
        # 2012
        if y_selected == 1:
            title = f"Year: 2012"
            total_sales = "$100,000,000"

        # 2013
        if y_selected == 2:
            title = f"Year: 2013"
            total_sales = "$100,000,000"

        # 2014
        if y_selected == 3:
            title = f"Year: 2014"
            total_sales = "$100,000,000"

        # 2015
        if y_selected == 4:
            title = f"Year: 2015"
            total_sales = "$100,000,000"

        # 2016
        if y_selected == 5:
            title = f"Year: 2016"
            total_sales = "$100,000,000"

        # 2017
        if y_selected == 6:
            title = f"Year: 2017"
            total_sales = "$100,000,000"

        # 2018
        if y_selected == 7:
            title = f"Year: 2018"
            total_sales = "$100,000,000"

        # 2019
        if y_selected == 8:
            title = f"Year: 2019"
            total_sales = "$100,000,000"

        # 2020
        if y_selected == 9:
            title = f"Year: 2020"
            total_sales = "$100,000,000"

        # 2021
        if y_selected == 10:
            title = f"Year: 2021"
            total_sales = "$100,000,000"

        # 2022
        if y_selected == 11:
            title = f"Year: 2022"
            total_sales = "$100,000,000"

    return title, total_sales

# -------------------------------------------------
@callback(
    Output('card_cost_title', 'children'),
    Output('card_total_cost', 'children'),
    Input('store_y', 'data'),
)
def selected_y(y_selected):
    global title, total_sales

    if y_selected is None:
        title = f"Year: N/A"
        total_sales = "$0"
    else:
        # 2012
        if y_selected == 1:
            title = f"Year: 2012"
            total_sales = "$100,000,000"

        # 2013
        if y_selected == 2:
            title = f"Year: 2013"
            total_sales = "$100,000,000"

        # 2014
        if y_selected == 3:
            title = f"Year: 2014"
            total_sales = "$100,000,000"

        # 2015
        if y_selected == 4:
            title = f"Year: 2015"
            total_sales = "$100,000,000"

        # 2016
        if y_selected == 5:
            title = f"Year: 2016"
            total_sales = "$100,000,000"

        # 2017
        if y_selected == 6:
            title = f"Year: 2017"
            total_sales = "$100,000,000"

        # 2018
        if y_selected == 7:
            title = f"Year: 2018"
            total_sales = "$100,000,000"

        # 2019
        if y_selected == 8:
            title = f"Year: 2019"
            total_sales = "$100,000,000"

        # 2020
        if y_selected == 9:
            title = f"Year: 2020"
            total_sales = "$100,000,000"

        # 2021
        if y_selected == 10:
            title = f"Year: 2021"
            total_sales = "$100,000,000"

        # 2022
        if y_selected == 11:
            title = f"Year: 2022"
            total_sales = "$100,000,000"

    return title, total_sales

# -------------------------------------------------
@callback(
    Output('card_retail_title', 'children'),
    Output('card_total_retail', 'children'),
    Input('store_y', 'data'),
)
def selected_y(y_selected):
    global title, total_sales

    if y_selected is None:
        title = f"Year: N/A"
        total_sales = "$0"
    else:
        # 2012
        if y_selected == 1:
            title = f"Year: 2012"
            total_sales = "$100,000,000"

        # 2013
        if y_selected == 2:
            title = f"Year: 2013"
            total_sales = "$100,000,000"

        # 2014
        if y_selected == 3:
            title = f"Year: 2014"
            total_sales = "$100,000,000"

        # 2015
        if y_selected == 4:
            title = f"Year: 2015"
            total_sales = "$100,000,000"

        # 2016
        if y_selected == 5:
            title = f"Year: 2016"
            total_sales = "$100,000,000"

        # 2017
        if y_selected == 6:
            title = f"Year: 2017"
            total_sales = "$100,000,000"

        # 2018
        if y_selected == 7:
            title = f"Year: 2018"
            total_sales = "$100,000,000"

        # 2019
        if y_selected == 8:
            title = f"Year: 2019"
            total_sales = "$100,000,000"

        # 2020
        if y_selected == 9:
            title = f"Year: 2020"
            total_sales = "$100,000,000"

        # 2021
        if y_selected == 10:
            title = f"Year: 2021"
            total_sales = "$100,000,000"

        # 2022
        if y_selected == 11:
            title = f"Year: 2022"
            total_sales = "$100,000,000"

    return title, total_sales