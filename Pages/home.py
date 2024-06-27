from dash import Dash,html, dcc, callback, Input, Output, ctx
import dash_bootstrap_components as dbc
import dash
import pandas as pd
import numpy as np

dash.register_page(__name__, path="/", order=0)

card_icon = {
    "color": "primary",
    "textAlign": "center",
    "fontSize": 80,
    "margin": "auto",
}
data = pd.read_csv('HR data.csv')

updateTime = (
    f"Last Update on {pd.to_datetime(pd.Timestamp.today()).strftime('%Y-%m-%d')}"
)
NbrEmploye = f'{data.shape[0]}'
Departs = f"{data[data['Attrition']=='Yes'].shape[0]}"
Actifs = f"{data[data['Attrition']!='Yes'].shape[0]}"
taux_depart = f"{np.round(data[data['Attrition']=='Yes'].shape[0]/data.shape[0]*100,2)} %"
age_moyen = f"{int(np.round(data['Age'].mean(),0))}"

def create_card(ico, title, value, note):
    card = dbc.CardGroup(
        [
            dbc.Card(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                # dbc.CardImg(
                                #     src=dash.get_asset_url("VOST_LOGO.png"),
                                #     className="img-fluid rounded-start",
                                # ),
                                html.I(className=ico),
                                className="col-md-4 ",
                                style=card_icon,
                            ),
                            dbc.Col(
                                dbc.CardBody(
                                    [
                                        html.H4(title, className="card-title"),
                                        html.H1(
                                            value,
                                            className="card-text",
                                        ),
                                        html.Small(
                                            note,
                                            className="card-text text-muted",
                                        ),
                                    ]
                                ),
                                className="col-md-8 ",
                            ),
                        ],
                        className="g-0 d-flex align-items-center",
                    )
                ],
                className="mb-3 bg-opacity-10  mt-3 shadow my-2 bg-light text-primary  rounded  ",
            ),
            dbc.Card(
                className="mb-3 mt-3 bg-primary shadow my-2 bg-opacity-80  ",
                style={"maxWidth": 75},
            ),
        ],
        className="",
    )

    return card
# create card instances
card1 = create_card(
    "bi bi-sunrise-fill me-2",
    "Active Since",
    "January 2023",
    "A new tool against disinformation",
)
card2 = create_card(
    "bi bi-graph-up-arrow  me-2", "Active Users", NbrEmploye, updateTime
)
card3 = create_card(
    "bi bi-file-text-fill me-2", "Submitted Reports", Departs, updateTime
)
card4 = create_card("bi bi-trophy-fill me-2", "Success Rate", Actifs, updateTime)
card5 = create_card(
    "bi bi bi-clock-history me-2", "Avg Turnaround Time", taux_depart, updateTime
)
card5 = create_card(
    "bi bi bi-clock-history me-2", "Avg Turnaround Time", age_moyen, updateTime
)

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.SPACELAB, dbc.icons.BOOTSTRAP],
    use_pages=True,
    pages_folder="pages",
    prevent_initial_callbacks=True,
    suppress_callback_exceptions=True,
)

layout = dbc.Container(
    [
        dcc.Interval(
            id="card_interval-id",
            disabled=False,
            n_intervals=0,
            interval=1 * 3000,
        ),
        dbc.Row(
            [
                dbc.Col([
                    dbc.Container(
                        html.Img(
                            src=dash.get_asset_url("rh_logo.jpg"),
                            style={
                                    "margin-left": "auto",
                                    "margin-right": "auto",
                                    "display": "block",
                                    "width": "100%",
                                },
                            ),
                        className="p-2 ",
                        fluid=False,
                    ),
            ])
            ],align="center",
        ),
        dbc.Row([

        ])
    ]
)
