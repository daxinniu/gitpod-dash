import dash
from dash import dcc # dash core components
from dash import html

from dash.dependencies import Input, Output

import numpy as np
import sympy

app = dash.Dash(__name__)

app.layout = html.Div(
    className="main",
    children=[
        html.H2("Grapher"),
        dcc.Input(id="input", value='x**2'),
        dcc.Graph(
            id='graph',
            figure={
                'data': [
                    {'x': np.linspace(0, 3, 100),
                     'y': np.linspace(0, 3, 100)**2,
                     'type': 'line'},
                ]
            }
        )
    ]
)

@app.callback(
    Output(component_id='graph', component_property='figure'),
    Input(component_id='input', component_property='value')
)
def update_graph(input_expression):
    try:
        x = sympy.symbols("x")
        f = sympy.lambdify(
            x,
            sympy.parse_expr(input_expression),
        )
        return {
            'data': [
                {'x': np.linspace(0, 3, 100),
                 'y': [f(x) for x in np.linspace(0, 3, 100)],
                 'type': 'line'},
            ]
        }
    except:
        return {}

app.run_server(debug=True, host="0.0.0.0")