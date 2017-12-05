# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, Event
import model as m

# Run with: python app.py
answers = {}

# Setup app
app = dash.Dash()

external_css = ["https://fonts.googleapis.com/css?family=Overpass:300,300i",
                "https://cdn.rawgit.com/plotly/dash-app-stylesheets/dab6f937fd5548cebf4c6dc7e93a10ac438f5efb/dash-technical-charting.css"]

for css in external_css:
    app.css.append_css({"external_url": css})

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

                html.Label('Do you live in an apartment?'),
                dcc.RadioItems(
                    id='apartment',
                    options=[
                        {'label': 'Yes', 'value': 1},
                        {'label': 'No', 'value': 0}
                    ],
                    #labelStyle={'display': 'inline-block'}
                ),

                html.Label('Would your dog be alone a lot?'),
                dcc.RadioItems(
                    id='alone',
                    options=[
                        {'label': 'Yes', 'value': 1},
                        {'label': 'No', 'value': 0}
                    ],
                    #labelStyle={'display': 'inline-block'}
                ),

                html.Label('Does your dog need to tolerate warm weather?'),
                dcc.RadioItems(
                    id='warm',
                    options=[
                        {'label': 'Yes', 'value': 1},
                        {'label': 'No', 'value': 0}
                    ],
                    #labelStyle={'display': 'inline-block'}
                ),

                html.Label('Does your dog need to tolerate cold weather?'),
                dcc.RadioItems(
                    id='cold',
                    options=[
                        {'label': 'Yes', 'value': 1},
                        {'label': 'No', 'value': 0}
                    ],
                    #labelStyle={'display': 'inline-block'}
                ),
            ],
            style={'columnCount': 4},
        ),

        html.Hr(style={'margin': '5', 'margin-bottom': '5'}),
        html.Div([html.H6('Personality')]),
        html.Div('Do you require a dog that is...'),

        html.Div( 
            [

                html.Label('...affectionate with family?'),
                dcc.RadioItems(
                    id='family',
                    options=[
                        {'label': 'Yes', 'value': 1},
                        {'label': 'No', 'value': 0}
                    ],
                    #labelStyle={'display': 'inline-block'}
                ),

                html.Label('...friendly with kids?'),
                dcc.RadioItems(
                    id='kids',
                    options=[
                        {'label': 'Yes', 'value': 1},
                        {'label': 'No', 'value': 0}
                    ],
                    #labelStyle={'display': 'inline-block'}
                ),

                html.Label('...friendly with other dogs?'),
                dcc.RadioItems(
                    id='otherdogs',
                    options=[
                        {'label': 'Yes', 'value': 1},
                        {'label': 'No', 'value': 0}
                    ],
                    #labelStyle={'display': 'inline-block'}
                ),

                html.Label('...friendly toward strangers?'),
                dcc.RadioItems(
                    id='strangers',
                    options=[
                        {'label': 'Yes', 'value': 1},
                        {'label': 'No', 'value': 0}
                    ],
                    #labelStyle={'display': 'inline-block'}
                )

            ],
            style={'columnCount': 4},
        ),


        html.Hr(style={'margin': '5', 'margin-bottom': '5'}),
        html.Div([html.H6('Energy Level')]),

        html.Div( 
            [


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

                html.Label('Will you be able to regularly exercise your dog?'),
                dcc.RadioItems(
                    id='exercise',
                    options=[
                        {'label': 'Yes', 'value': 1},
                        {'label': 'No', 'value': 0}
                    ],
                    #labelStyle={'display': 'inline-block'}
                ),


                html.Label('Is it important that your dog is playful?'),
                dcc.RadioItems(
                    id='playful',
                    options=[
                        {'label': 'Yes', 'value': 1},
                        {'label': 'No', 'value': 0}
                    ],
                    #labelStyle={'display': 'inline-block'}
                ),



                


            ],
            style={'columnCount': 4},
        ),

        html.Hr(style={'margin': '5', 'margin-bottom': '5'}),
        html.Div([html.H6('Training & Care')]),
        html.Div('Is it important that your dog...'),

        html.Div( 
            [

                html.Label('...is easy to train?'),
                dcc.RadioItems(
                    id='train',
                    options=[
                        {'label': 'Yes', 'value': 1},
                        {'label': 'No', 'value': 0}
                    ],
                    #labelStyle={'display': 'inline-block'}
                ),


                html.Label('...is easy to groom?'),
                dcc.RadioItems(
                    id='groom',
                    options=[
                        {'label': 'Yes', 'value': 1},
                        {'label': 'No', 'value': 0}
                    ],
                    #labelStyle={'display': 'inline-block'}
                ),

                html.Label('...does not shed much?'),
                dcc.RadioItems(
                    id='shed',
                    options=[
                        {'label': 'Yes', 'value': 1},
                        {'label': 'No', 'value': 0}
                    ],
                    #labelStyle={'display': 'inline-block'}
                ),

                html.Label('...does not drool much?'),
                dcc.RadioItems(
                    id='drool',
                    options=[
                        {'label': 'Yes', 'value': 1},
                        {'label': 'No', 'value': 0}
                    ],
                    #labelStyle={'display': 'inline-block'}
                ),




            ],
            style={'columnCount': 4},
        ),

        html.Hr(style={'margin': '5', 'margin-bottom': '5'}),
        html.Div([html.H6('Skill & Preferences')]),

        html.Div( 
            [

                html.Label('Are you a novice dog owner?'),
                dcc.RadioItems(
                    id='novice',
                    options=[
                        {'label': 'Yes', 'value': 1},
                        {'label': 'No', 'value': 0}
                    ],
                    #labelStyle={'display': 'inline-block'}
                ),


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

                html.Label('Is it important that your dog does not bark frequently?'),
                dcc.RadioItems(
                    id='bark',
                    options=[
                        {'label': 'Yes', 'value': 1},
                        {'label': 'No', 'value': 0}
                    ],
                    labelStyle={'display': 'inline-block'}
                ),


            ],
            style={'columnCount': 4},
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
@app.callback(Output('table', 'children'), [
    Input('getResults', 'n_clicks')
    ])

def table_update(num_clicks):
    if (num_clicks>0):
        return generate_table()

def generate_table():
    #updateAnswers() TODO:
    dataframe = getResults(answers)
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
    return m.createTable(answer_dict)

# Read Quiz Answers
# TODO:



if __name__ == '__main__':
    app.run_server(debug=True)