import dash_bootstrap_components as dbc
from dash import html, callback, Output, Input

sale = [
    dbc.CardHeader(id="year_sale_title"),
    dbc.CardBody(
        [
            html.H5("$100,000,000",
                    className="card-title", style={"color": "#BF00BF"}),
            html.P("Total Sales (USD)", className="card-text fw-bold")
        ]
    ),
]

inv = [
    dbc.CardHeader(id="year_inv_title"),
    dbc.CardBody(
        [
            html.H5("$100,000,000",
                    className="card-title", style={"color": "#BF00BF"}),
            html.P("Number of invoices", className="card-text fw-bold")
        ]
    ),
]

bottlesold = [
    dbc.CardHeader(id="year_bottle_title"),
    dbc.CardBody(
        [
            html.H5("$100,000,000",
                    className="card-title", style={"color": "#BF00BF"}),
            html.P("Bottle Sold", className="card-text fw-bold")
        ]
    ),
]

volumesold = [
    dbc.CardHeader(id="year_volume_title"),
    dbc.CardBody(
        [
            html.H5("$100,000,000",
                    className="card-title", style={"color": "#BF00BF"}),
            html.P("Volume Sold (Gallons)", className="card-text fw-bold")
        ]
    ),
]

statebottlecost = [
    dbc.CardHeader(id="year_cost_title"),
    dbc.CardBody(
        [
            html.H5("$100,000,000",
                    className="card-title", style={"color": "#BF00BF"}),
            html.P("State Bottle Cost", className="card-text fw-bold")
        ]
    ),
]

statebottleretail = [
    dbc.CardHeader(id="year_retail_title"),
    dbc.CardBody(
        [
            html.H5("$100,000,000",
                    className="card-title", style={"color": "#BF00BF"}),
            html.P("State Bottle Retail", className="card-text fw-bold")
        ]
    ),
]

# -------------------------------------------------
@callback(
    Output('year_sale_title', 'children'),
    Input('store_y', 'data'),
)
def selected_y(y):
    return y

# -------------------------------------------------
@callback(
    Output('year_inv_title', 'children'),
    Input('store_y', 'data'),
)
def selected_y(y):
    return y

# -------------------------------------------------
@callback(
    Output('year_bottle_title', 'children'),
    Input('store_y', 'data'),
)
def selected_y(y):
    return y

# -------------------------------------------------
@callback(
    Output('year_volume_title', 'children'),
    Input('store_y', 'data'),
)
def selected_y(y):
    return y

# -------------------------------------------------
@callback(
    Output('year_cost_title', 'children'),
    Input('store_y', 'data'),
)
def selected_y(y):
    return y

# -------------------------------------------------
@callback(
    Output('year_retail_title', 'children'),
    Input('store_y', 'data'),
)
def selected_y(y):
    return y