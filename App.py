import pandas as pd
import numpy as np
from dash import html
from dash import dcc
import dash
import dash_bootstrap_components as dbc
import warnings
from dash import dash_table as dt
from dash.dash_table.Format import Format, Group
import plotly.express as px
from datetime import date

data = pd.read_csv('HR data.csv')

# print(data.head())

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
                    dbc.Row([
                        dbc.Card(
                            dbc.CardBody([
                                dbc.Col([html.A([html.Img(src=app.get_asset_url('ut_logo.png'),
                                  style={'height':'60px','width':'auto'}
                                  )])
                                ],width={'size':2}),
                                dbc.Col([
                                    html.H1('DASBOARD RH',style={'textAlign':'right',
                                                                   'color':'Back'})
                                ],width={'size':6,'offset':1})
                            ]),
                            color="#8B5959"
                        )
                    ]),
                    html.Br(),
                    dbc.Row(
                        dbc.Col([
                                dbc.Card(
                                    dbc.CardBody([
                                        html.H4('Nombre d\'employés',style={'textAlign': 'center'}),
                                        html.P(f'{data.shape[0]}',
                                                style={'textAlign': 'center',
                                                        'color': 'black',
                                                        'fontSize': 32})]),
                                    color="#8B5959"
                                )

                            ],width={'size': 2}),

                    )
],style={'backgroundColor': '#B79F9F'})



if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8022)