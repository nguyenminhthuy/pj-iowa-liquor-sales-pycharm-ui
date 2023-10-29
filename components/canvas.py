import dash_bootstrap_components as dbc
from dash import html, dcc

btn_filter = html.Span([html.I(className="fa fa-search fa-lg"), " Filter Data"])

off_canvas = html.Div(
    [
        dbc.Button(children=btn_filter,
                   id="open-offcanvas-scrollable",
                   n_clicks=0, style=dict(fontSize="20px", backgroundColor="rgb(237, 201, 72)",
                                          textAlign="center", color="black", border="none")
                   ),
        dbc.Offcanvas([
                html.Div([
                        html.P("Year"),
                        dcc.Dropdown(
                            ['2012', '2013', '2014','2015','2016','2017','2018','2019','2020','2021','2022'],
                            placeholder="Select...", multi=True
                        )], className="mb-3"),
                html.Div([
                        html.P("Item name"),
                        dcc.Dropdown(
                            ['New York City', 'Montreal', 'San Francisco'],
                            placeholder="Select...", multi=True
                        )], className="mb-3"),
                html.Div([
                        html.P("Store name"),
                        dcc.Dropdown(
                            ['New York City', 'Montreal', 'San Francisco'],
                            placeholder="Select...", multi=True
                        )], className="mb-3"),
                html.Div([
                        html.P("Category name"),
                        dcc.Dropdown(
                            ['New York City', 'Montreal', 'San Francisco'],
                            placeholder="Select...", multi=True
                        )], className="mb-3"),
                html.Div([
                        html.P("Vendor name"),
                        dcc.Dropdown(
                            ['New York City', 'Montreal', 'San Francisco'],
                            placeholder="Select...", multi=True
                        )], className="mb-3"),
                html.Div([
                        dbc.Button("SUBMIT",
                                   href="/search",
                                   className='btn-search p-2',
                                   style={
                                       'background-color': 'rgb(237, 201, 72)',
                                       'color': 'rgb(30, 51, 118)',
                                       'border': '0px', 'font-weight': 'bold'
                                   })
                     ], className="m-4 d-grid gap-3"),
            ],
            id="offcanvas-scrollable",
            scrollable=True,
            title="FILTER DATA",
            is_open=False,
        ),
    ]
)
