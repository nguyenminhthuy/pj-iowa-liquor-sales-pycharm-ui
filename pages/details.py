import dash_bootstrap_components as dbc
from dash import html, callback, Output, Input, dcc

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
            # SALES ANALYSIS OVERVIEW
            dbc.Badge("Success", color="success", className="me-1"),
            html.H3(id="overview_title", style={"color": "#FF7F50"}),
            dbc.Col(dbc.Card(cards.sale, color="info", outline=True, className="shadow")),
            dbc.Col(dbc.Card(cards.cost_sales, color="info", outline=True, className="shadow")),
            dbc.Col(dbc.Card(cards.gross_profit, color="info", outline=True, className="shadow")),
            dbc.Col(dbc.Card(cards.inv, color="info", outline=True, className="shadow")),
            dbc.Col(dbc.Card(cards.bottleSold, color="info", outline=True, className="shadow")),
            dbc.Col(dbc.Card(cards.volumeSold, color="info", outline=True, className="shadow"))
        ], className="m-4",
    ),

    dbc.Row(
        [
            dbc.Col(cards.month_graph, className="text-center border-end m-3"),
            dbc.Col(cards.m_dow_graph, className="text-center border-end m-3"),
            dbc.Col(cards.dow_graph, className="text-center border-end m-3"),
        ], className="m-4",
    ),

    html.Div(
        dbc.Row([
                dbc.Col(html.H3("SALES ANALYSIS", style={"color": "#FF7F50"})),
            ], className="m-5"
        )
    ),

    html.Div(
        dbc.Row([
            dbc.Col([
                dcc.Tabs([
                    dcc.Tab(label='TOP 10 ITEMS', children=[
                        dbc.Row([
                            dbc.Col(cards.top_highestItem_graph, className="m-4"),
                            dbc.Col(cards.top_mostItem_graph, className="m-3"),
                        ])
                    ], style=tab_style, selected_style=tab_selected_style),

                    dcc.Tab(label='TOP 10 CATEGORIES', children=[
                        dbc.Row([
                            dbc.Col(cards.top_highestCat_graph, className="m-4"),
                            dbc.Col(cards.top_mostCat_graph, className="m-4"),
                        ])
                    ], style=tab_style, selected_style=tab_selected_style),

                    dcc.Tab(label='TOP 10 VENDORS', children=[
                        dbc.Row([
                            dbc.Col(cards.top_highestVendor_graph, className="m-4"),
                            dbc.Col(cards.top_mostVendor_graph, className="m-4"),
                        ])
                    ], style=tab_style, selected_style=tab_selected_style),

                    dcc.Tab(label='TOP 10 STORES', children=[
                        dbc.Row([
                            dbc.Col(cards.top_highestStore_graph, className="m-4"),
                            dbc.Col(cards.top_mostStore_graph, className="m-4"),
                        ])
                    ], style=tab_style, selected_style=tab_selected_style),
                ])
            ])
        ], className="m-5"
        )
    ),

    dbc.Row(
        [
            html.H3("STORE LOCATION", style={"color": "#FF7F50"}),
            html.Div(id='folium-map-container')
        ], className="m-5",
    ),
])


@callback(
    Output('overview_title', 'children'),
    Output('folium-map-container', 'children'),
    Input('store_y', 'data'),
)
def selected_y(y_selected):
    global overview_title, folium_map

    if y_selected is None:
        overview_title = f"SALES ANALYSIS OVERVIEW (N/A)"
        folium_map = html.Iframe(srcDoc = open('img/map_2012.html', 'r').read(),
                                 width='100%', height=500)
    else:
        # 2012
        if y_selected == 1:
            overview_title = f"SALES ANALYSIS OVERVIEW (2012)"
            folium_map = html.Iframe(srcDoc=open('img/map_2012.html', 'r').read(),
                                     width='100%', height=500)

        # 2013
        if y_selected == 2:
            overview_title = f"SALES ANALYSIS OVERVIEW (2013)"
            folium_map = html.Iframe(srcDoc=open('img/map_2012.html', 'r').read(),
                                     width='100%', height=500)

        # 2014
        if y_selected == 3:
            overview_title = f"SALES ANALYSIS OVERVIEW (2014)"
            folium_map = html.Iframe(srcDoc=open('img/map_2012.html', 'r').read(),
                                     width='100%', height=500)

        # 2015
        if y_selected == 4:
            overview_title = f"SALES ANALYSIS OVERVIEW (2015)"
            folium_map = html.Iframe(srcDoc=open('img/map_2012.html', 'r').read(),
                                     width='100%', height=500)

        # 2016
        if y_selected == 5:
            overview_title = f"SALES ANALYSIS OVERVIEW (2016)"
            folium_map = html.Iframe(srcDoc=open('img/map_2012.html', 'r').read(),
                                     width='100%', height=500)

        # 2017
        if y_selected == 6:
            overview_title = f"SALES ANALYSIS OVERVIEW (2017)"
            folium_map = html.Iframe(srcDoc=open('img/map_2012.html', 'r').read(),
                                     width='100%', height=500)

        # 2018
        if y_selected == 7:
            overview_title = f"SALES ANALYSIS OVERVIEW (2018)"
            folium_map = html.Iframe(srcDoc=open('img/map_2012.html', 'r').read(),
                                     width='100%', height=500)

        # 2019
        if y_selected == 8:
            overview_title = f"SALES ANALYSIS OVERVIEW (2019)"
            folium_map = html.Iframe(srcDoc=open('img/map_2012.html', 'r').read(),
                                     width='100%', height=500)

        # 2020
        if y_selected == 9:
            overview_title = f"SALES ANALYSIS OVERVIEW (2020)"
            folium_map = html.Iframe(srcDoc=open('img/map_2012.html', 'r').read(),
                                     width='100%', height=500)

        # 2021
        if y_selected == 10:
            overview_title = f"SALES ANALYSIS OVERVIEW (2021)"
            folium_map = html.Iframe(srcDoc=open('img/map_2012.html', 'r').read(),
                                     width='100%', height=500)

        # 2022
        if y_selected == 11:
            overview_title = f"SALES ANALYSIS OVERVIEW (2022)"
            folium_map = html.Iframe(srcDoc=open('img/map_2012.html', 'r').read(),
                                     width='100%', height=500)

    return overview_title, folium_map
