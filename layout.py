import os
from dash_bootstrap_components._components.NavbarSimple import NavbarSimple
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go
from stockdata import SYMBOLS, MIN_DATE, MAX_DATE
options = [{"label": tic, "value": tic} for tic in SYMBOLS]
about_dashboard = html.Div(
    children=[
        html.A(
            [html.I(className="fa fa-bar-chart mx-1"), "Data Source (yfinance)"],
            href="https://finance.yahoo.com/",
            className="btn btn-outline-info shadow mb-3 mr-2",        ),      
  
        html.P(
            """
        To save any plot locally, use the camera icon in top left. 
        """
        ),
        html.P(
            """
        All plots are interactive -hover over charts, lines & points 
        for tooltips (dynamic annotations), zoom using your mouse (drag to select area to 
        zoom into), and double click to zoom out & reset. 
        """
        ),
    ]
)
modal = html.Div(
    [
        dbc.Button(
            "About the Dashboard", id="open", n_clicks=0, className="btn btn-info"
        ),
        dbc.Modal(
            [
                dbc.ModalHeader("Visualize and forecast stocks| yfinance"),
                dbc.ModalBody(children=about_dashboard),
                dbc.ModalFooter(
                    dbc.Button("Close", id="close", className="ml-auto", n_clicks=0)
                ),
            ],
            id="modal",
            is_open=False,
            size="lg",
        ),
    ]
)
navbar = NavbarSimple(
    className="shadow text-white",
    children=[
        # dbc.NavLink("About the Dashboard", className="btn btn-info text-white", id='open'),
        modal,
    ],
    brand="Stock Dashboard",
    brand_href="/",
    color="dark",
    dark=True,
)
layout_1 = dbc.Row(
    className="text-center m-4 justify-content-around",
    children=[        dbc.Col(
            style={"minHeight": "520px"},
            className="card-body col-md-6 my-sm-3 col-sm-12 shadow",
            children=[
                html.Div(
                    [
                        html.Div(
                            [
                                html.P(
                                    [
                                        html.I(className="fa fa-line-chart mr-1"),
                                        "Select a stock symbol",
                                    ],
                                    className="d-inline mr-2",
                                ),
                                dcc.Dropdown(
                                    id="ticker",
                                    options=options,
                                    value=options[0]["label"],
                                    className="text-dark",
                                ),
                            ],
                            className="d-inline col-md-6",
                        ),
                        html.Div(
                            [
                                dcc.Checklist(
                                    id="toggle-rangeslider",
                                    options=[
                                        {
                                            "label": "Include Rangeslider",
                                            "value": "slider",
                                        }
                                    ],
                                    value=["slider"],
                                    className="d-inline",
                                ),
                            ],
                            className="d-inline col-md-6",
                        ),
                    ],
                    className="bg-dark text-white",
                ),
                dcc.Loading(
                    id="loading_graph1",
                    children=[
                        dcc.Graph(
                            id="graph1",
                            figure=go.Figure([go.Candlestick()]),
                            style={"height": "390px"},
                        )
                    ],
                    type="default",
                ),
            ],
        ),
        dbc.Col(
            style={"minHeight": "520px"},
            className="card-body col-md-5 my-sm-3 col-sm-12 shadow",
            children=[
                html.Div(
                    [
                        html.Div(
                            [
                                html.P(
                                    [
                                        html.I(className="fa fa-line-chart mr-1"),
                                        "Select stock symbol",
                                    ],
                                    className="d-inline mr-2",
                                ),
                                dcc.Dropdown(
                                    id="multi_tickers",
                                    options=options,
                                    value=[op["label"] for op in options[:2]],
                                    className="text-dark",
                                    multi=True,
                                ),
                            ],
                            className="d-inline col-md-6",
                        ),
                        html.Div(
                            [
                                dcc.Checklist(
                                    id="toggle-rangeslider2",
                                    options=[
                                        {
                                            "label": "Include Rangeslider",
                                            "value": "slider",
                                        }
                                    ],
                                    value=["slider"],
                                    className="d-inline",
                                ),
                            ],
                            className="d-inline col-md-6",
                        ),
                    ],
                    className="bg-dark text-white",
                ),
                dcc.Loading(
                    id="loading_graph2",
                    children=[
                        dcc.Graph(
                            id="line_chart",
                            figure=go.Figure([go.Scatter()]),
                            style={"height": "390px"},
                        )
                    ],
                    type="default",
                ),
            ],
        ),
    ],
)
layout_2 = dbc.Row(
    className="text-center m-4 justify-content-around",
    children=[
        dbc.Col(
            style={"minHeight": "536px"},
            className="card-body col-md-6 col-sm-12 shadow",
            children=[
                html.Div(
                    [
                        html.Div(
                            [
                                html.P(
                                    [
                                        html.I(className="fa fa-line-chart mr-1"),
                                        "Select stock symbol",
                                    ],
                                    className="d-inline mr-2",
                                ),
                                dcc.Dropdown(
                                    id="bar_ticker",
                                    options=options,
                                    value=options[0]["label"],
                                    className="text-dark",
                                ),
                                html.Div(
                                    [
                                        dcc.DatePickerRange(
                                            id="bar_date_picker",
                                            min_date_allowed=MIN_DATE,
                                            max_date_allowed=MAX_DATE,
                                            start_date=MAX_DATE - pd.Timedelta(days=3),
                                            end_date=MAX_DATE,
                                            className="d-inline",
                                        ),
                                    ],
                                    className="d-inline col-md-6",
                                ),
                            ],
                            className="d-inline col-md-6",
                        ),
                    ],
                    className="bg-dark text-white",
                ),
                dcc.Graph(
                    id="bar_graph",
                    style={"height": "390px"},
                ),
            ],
        ),
        dbc.Col(
            style={"minHeight": "536px"},
            className="card-body col-md-5 col-sm-12 shadow",
            children=[
                html.Div(
                    [
                        html.Div(
                            [
                                html.P(
                                    [
                                        html.I(className="fa fa-line-chart mr-1"),
                                        "Select stock symbol",
                                    ],
                                    className="d-inline mr-2",
                                ),
                                dcc.Dropdown(
                                    id="pie_tickers",
                                    options=options,
                                    value=[op["label"] for op in options[:3]],
                                    className="text-dark",
                                    multi=True,
                                ),
                            ],
                            className="d-inline col-md-6",
                        ),
                        html.Div(
                            [
                                dcc.DatePickerSingle(
                                    id="pie_date_picker_single",
                                    min_date_allowed=MIN_DATE,
                                    max_date_allowed=MAX_DATE,
                                    date=MAX_DATE,
                                    className="d-inline",
                                ),
                            ],
                            className="d-inline col-md-6",
                        ),
                    ],
                    className="bg-dark text-white",
                ),
                dcc.Graph(
                    id="pie_chart",
                    style={"height": "390px"},
                ),
            ],
        ),
    ],
)

footer = html.Div(
    className="bg-dark shadow text-white text-center mt-5 p-3",
    children=[
        html.P("©All copyrights are reserved", className="mt-2"),
    ],
)
