# -*- coding: utf-8 -*-
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, Event, State
import model as m
import os

scriptdir = os.path.dirname(os.path.realpath(__file__))
datadir = os.path.join(scriptdir,'scraper')
all_ratings_path = os.path.join(datadir,'all_ratings.csv')

# import ratings
ratings_df = pd.read_csv(all_ratings_path)
ratings_df.set_index('Breed',inplace=True)

# Run with: python app.py
answers = {}

# Setup app
app = dash.Dash()

external_css = ["https://fonts.googleapis.com/css?family=Overpass:300,300i",
                "https://cdn.rawgit.com/plotly/dash-app-stylesheets/dab6f937fd5548cebf4c6dc7e93a10ac438f5efb/dash-technical-charting.css"]

for css in external_css:
    app.css.append_css({"external_url": css})

row_style4 = {
    'height':'120px',
    'width':'100%',
    'whiteSpace':'nowrap',
    'textAlign':'center',
    'margin':'1em 0',
    'columnCount':4}

row_style3 = {
    'height':'120px',
    'width':'100%',
    'whiteSpace':'nowrap',
    'textAlign':'center',
    'margin':'1em 0',
    'columnCount':3}

question_style = {
    'maxWidth':'100px',
    'maxHeight':'120px',
    'verticalAlign':'middle',
    'margin-left':'2%',
    'margin-right':'2%'}

# Define App Layout
app.layout = html.Div(
    [
        html.Div(
            [
                html.H1(children='Dog Breed Recommendations'),

                html.Div(children='''
                    Welcome to our site! To find your personalized top dog breed matches, take the quiz below.
                '''),

                # https://community.plot.ly/t/html-button-adding-a-click-event/5073
                html.Button('Reset Quiz', id='reset')


            ]
        ),


        html.Hr(style={'margin': '5', 'margin-bottom': '5'}),
        html.Hr(style={'margin': '5', 'margin-bottom': '5'}),

        html.Div([html.H6('Lifestyle')]),

        html.Div(
            [
                html.Div([
                    html.Label('Do you live in an apartment?'),
                    dcc.RadioItems(
                        id='apartment',
                        options=[
                            {'label': 'Yes', 'value': 1},
                            {'label': 'No', 'value': 0}
                        ],
                        #labelStyle={'display': 'inline-block'}
                    ),
                ],style=question_style),

                html.Div([
                    html.Label('Would your dog be alone a lot?'),
                    dcc.RadioItems(
                        id='alone',
                        options=[
                            {'label': 'Yes', 'value': 1},
                            {'label': 'No', 'value': 0}
                        ],
                        #labelStyle={'display': 'inline-block'}
                    ),
                ],style=question_style),

                html.Div([
                    html.Label('Does your dog need to tolerate warm weather?'),
                    dcc.RadioItems(
                        id='warm',
                        options=[
                            {'label': 'Yes', 'value': 1},
                            {'label': 'No', 'value': 0}
                        ],
                        #labelStyle={'display': 'inline-block'}
                    ),
                ],style=question_style),

                html.Div([
                    html.Label('Does your dog need to tolerate cold weather?'),
                    dcc.RadioItems(
                        id='cold',
                        options=[
                            {'label': 'Yes', 'value': 1},
                            {'label': 'No', 'value': 0}
                        ],
                        #labelStyle={'display': 'inline-block'}
                    ),
                ],style=question_style),
            ],style=row_style4,
        ),

        html.Hr(style={'margin': '5', 'margin-bottom': '5'}),
        html.Div([html.H6('Personality')]),
        html.Div('Do you require a dog that is...'),

        html.Div(
            [
                html.Div([
                    html.Label('...affectionate with family?'),
                    dcc.RadioItems(
                        id='family',
                        options=[
                            {'label': 'Yes', 'value': 1},
                            {'label': 'No', 'value': 0}
                        ],
                        #labelStyle={'display': 'inline-block'}
                    ),
                ],style=question_style),

                html.Div([
                    html.Label('...friendly with kids?'),
                    dcc.RadioItems(
                        id='kids',
                        options=[
                            {'label': 'Yes', 'value': 1},
                            {'label': 'No', 'value': 0}
                        ],
                        #labelStyle={'display': 'inline-block'}
                    ),
                ],style=question_style),

                html.Div([
                    html.Label('...friendly with other dogs?'),
                    dcc.RadioItems(
                        id='otherdogs',
                        options=[
                            {'label': 'Yes', 'value': 1},
                            {'label': 'No', 'value': 0}
                        ],
                        #labelStyle={'display': 'inline-block'}
                    ),
                ],style=question_style),

                html.Div([
                    html.Label('...friendly toward strangers?'),
                    dcc.RadioItems(
                        id='strangers',
                        options=[
                            {'label': 'Yes', 'value': 1},
                            {'label': 'No', 'value': 0}
                        ],
                        #labelStyle={'display': 'inline-block'}
                    )
                ],style=question_style),

            ],
            style=row_style4,
        ),


        html.Hr(style={'margin': '5', 'margin-bottom': '5'}),
        html.Div([html.H6('Energy Level')]),

        html.Div(
            [
                html.Div([
                    html.Label('Do you prefer a low, medium, or high energy dog?'),
                    dcc.RadioItems(
                        id='energy',
                        options=[
                            {'label': 'Low', 'value': 'low'},
                            {'label': 'Medium', 'value': 'medium'},
                            {'label': 'High', 'value': 'high'}
                        ],
                        labelStyle={'display': 'inline-block'}
                    ),
                    html.Br()
                ],style=question_style),

                html.Div([
                    html.Label('Will you be able to regularly exercise your dog?'),
                    dcc.RadioItems(
                        id='exercise',
                        options=[
                            {'label': 'Yes', 'value': 1},
                            {'label': 'No', 'value': 0}
                        ],
                        #labelStyle={'display': 'inline-block'}
                    ),
                ],style=question_style),

                html.Div([
                    html.Label('Is it important that your dog is playful?'),
                    dcc.RadioItems(
                        id='playful',
                        options=[
                            {'label': 'Yes', 'value': 1},
                            {'label': 'No', 'value': 0}
                        ],
                        #labelStyle={'display': 'inline-block'}
                    ),
                ],style=question_style),

                # html.Div([
                #     # placeholder
                # ],style=question_style),

            ],
            style=row_style3,
        ),

        html.Hr(style={'margin': '5', 'margin-bottom': '5'}),
        html.Div([html.H6('Training & Care')]),
        html.Div('Is it important that your dog...'),

        html.Div(
            [
                html.Div([
                    html.Label('...is easy to train?'),
                    dcc.RadioItems(
                        id='train',
                        options=[
                            {'label': 'Yes', 'value': 1},
                            {'label': 'No', 'value': 0}
                        ],
                        #labelStyle={'display': 'inline-block'}
                    ),
                ],style=question_style),

                html.Div([
                    html.Label('...is easy to groom?'),
                    dcc.RadioItems(
                        id='groom',
                        options=[
                            {'label': 'Yes', 'value': 1},
                            {'label': 'No', 'value': 0}
                        ],
                        #labelStyle={'display': 'inline-block'}
                    ),
                ],style=question_style),

                html.Div([
                    html.Label('...does not shed much?'),
                    dcc.RadioItems(
                        id='shed',
                        options=[
                            {'label': 'Yes', 'value': 1},
                            {'label': 'No', 'value': 0}
                        ],
                        #labelStyle={'display': 'inline-block'}
                    ),
                ],style=question_style),

                html.Div([
                    html.Label('...does not drool much?'),
                    dcc.RadioItems(
                        id='drool',
                        options=[
                            {'label': 'Yes', 'value': 1},
                            {'label': 'No', 'value': 0}
                        ],
                        #labelStyle={'display': 'inline-block'}
                    ),
                ],style=question_style),

            ],
            style=row_style4,
        ),

        html.Hr(style={'margin': '5', 'margin-bottom': '5'}),
        html.Div([html.H6('Skill & Preferences')]),

        html.Div(
            [
                html.Div([
                    html.Label('Are you a novice dog owner?'),
                    dcc.RadioItems(
                        id='novice',
                        options=[
                            {'label': 'Yes', 'value': 1},
                            {'label': 'No', 'value': 0}
                        ],
                        #labelStyle={'display': 'inline-block'}
                    ),
                ],style=question_style),

                # html.Br(),

                html.Div([
                    html.Label('Do you have a preference for small, medium, or large dogs?'),
                    dcc.RadioItems(
                        id='size',
                        options=[
                            {'label': 'Small', 'value': 'small'},
                            {'label': 'Medium', 'value': 'medium'},
                            {'label': 'Large', 'value': 'large'}
                        ],
                        labelStyle={'display': 'inline-block'}
                    ),
                ],style=question_style),

                html.Br(),

                html.Div([
                    html.Label('Is it important that your dog does not bark frequently?'),
                    dcc.RadioItems(
                        id='bark',
                        options=[
                            {'label': 'Yes', 'value': 1},
                            {'label': 'No', 'value': 0}
                        ],
                        labelStyle={'display': 'inline-block'}
                    ),
                ],style=question_style),

                # html.Br(),

                # html.Div([
                #     # placeholder
                # ],style=question_style),

            ],
            style=row_style3,
        ),
        html.Hr(style={'margin': '5', 'margin-bottom': '5'}),
        html.Hr(style={'margin': '5', 'margin-bottom': '5'}),

        html.Div(
            [
                html.H4(children='Recommendations'),
                html.Button('Get my results!', id='getResults'),
            ]
        ),
        html.Div(id='hiddendiv'),
        #html.Div(id=‘hiddendiv’, style={‘display’:‘none’}),
        html.Div(
            [
                html.Table(id='table')
            ],
            #style={'width': '49%','display': 'inline-block', 'padding': '0 20'}
        )
    ]
)

# Reset all buttons
id_list = ['apartment','alone','warm','cold','family','kids','otherdogs','strangers','train','groom','shed','drool','energy','exercise','playful','novice','size','bark']

def create_reset_callback(output):
    def callback(input_value):
        if (input_value>0):
            return None

for id in id_list:
    new_callback = create_reset_callback(id)
    app.callback(Output(component_id=id,component_property='value'), [Input('reset', 'n_clicks')])(new_callback)

# Update Results
@app.callback(
    Output('table', 'children'),
    [Input('getResults', 'n_clicks')],
    [
        State('apartment', 'value'),
        State('alone', 'value'),
        State('warm', 'value'),
        State('cold', 'value'),
        State('family', 'value'),
        State('kids', 'value'),
        State('otherdogs', 'value'),
        State('strangers', 'value'),
        State('train', 'value'),
        State('groom', 'value'),
        State('shed', 'value'),
        State('drool', 'value'),
        State('energy', 'value'),
        State('exercise', 'value'),
        State('playful', 'value'),
        State('novice', 'value'),
        State('size', 'value'),
        State('bark', 'value'),
    ])

def table_update(num_clicks,i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18):
    if (num_clicks>0):
        updateAnswers(i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18)
        return generate_table()

def generate_table():
    dataframe = getResults(answers)
    #print(answers)
    max_rows=10
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )

# Get Results
def getResults(answer_dict):
    return m.createTable(answer_dict,ratings_df)

# Read Quiz Answers
def updateAnswers(*args):
    count=0
    for i in args:
        answers[id_list[count]] = i
        count+=1

if __name__ == '__main__':
    app.run_server(debug=True)
