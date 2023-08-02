import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output, State
from pages import (home, detail_2012, detail_2013, detail_2014, detail_2015, detail_2016, detail_2017, detail_2018,
                   detail_2019, detail_2020, detail_2021, detail_2022)
from components import navbar

app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP, "assets/style.css",
                          'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'],
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)
app.title = "IOWA LIQUOR SALES DASHBOARD"

content = html.Div(id="page-content", className='mt-0 mb-0')
app.layout = html.Div([dcc.Location(id="url"), navbar.header, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return home.layout
    elif pathname == "/detail-2012":
        return detail_2012.layout
    elif pathname == "/detail-2012":
        return detail_2012.layout
    elif pathname == "/detail-2013":
        return detail_2013.layout
    elif pathname == "/detail-2014":
        return detail_2014.layout
    elif pathname == "/detail-2015":
        return detail_2015.layout
    elif pathname == "/detail-2016":
        return detail_2016.layout
    elif pathname == "/detail-2017":
        return detail_2017.layout
    elif pathname == "/detail-2018":
        return detail_2018.layout
    elif pathname == "/detail-2019":
        return detail_2019.layout
    elif pathname == "/detail-2020":
        return detail_2020.layout
    elif pathname == "/detail-2021":
        return detail_2021.layout
    elif pathname == "/detail-2022":
        return detail_2022.layout
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )


@app.callback(
    Output("offcanvas-scrollable", "is_open"),
    Input("open-offcanvas-scrollable", "n_clicks"),
    State("offcanvas-scrollable", "is_open"),
)
def toggle_offcanvas_scrollable(n1, is_open):
    if n1:
        return not is_open
    return is_open


if __name__ == "__main__":
    app.run_server()
