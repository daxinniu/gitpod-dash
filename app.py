import dash
from dash import dcc # dash core components
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H2(children='Greetings!'),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [5, 7, 2], 'type': 'line'},
            ],
            'layout': {
                'title': 'Example Graph'
            }
        }
    ),
    dcc.Dropdown(
        id="city-dropdown",
        options=[
            {'label': 'Boston', 'value': 'BOS'},
            {'label': 'Montréal', 'value': 'MTL'},
            {'label': 'Providence', 'value': 'PVD'}
        ],
        multi=True,
        value="MTL"
    ),
    dcc.Slider(
        id='my-slider',
        min=0,
        max=20,
        step=0.5,
        value=10,
    ),
    dcc.Input(
        id='my-input',
        placeholder='Enter a value...',
        type='text',
        value=''
    )
])
app.run_server(debug=True, host="0.0.0.0")
