import dash
from dash import dcc
from dash import html
from dash import dash_table
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://bit.ly/elements-periodic-table')

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id="index-dropdown",
        options=[{'label': i, 'value': i} for i in df.columns],
        multi=True,
        value=df.columns
    ),
    dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
)
])
#[{"label": i, "value": df[i]} for i in df.columns]
@app.callback([
    Output('table', 'data'),
    Output('table', 'columns')
    ], 
    [Input('index-dropdown', 'value')])
def update_cols(cols):
    df1 = df[cols]
    out_cols = [{"name": i, "id": i} for i in cols]
    return df1.to_dict('records'), out_cols
'''
@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value'))
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]

    fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
                     size="pop", color="continent", hover_name="country",
                     log_x=True, size_max=55)
    fig.update_layout(transition_duration=500)
    return fig
'''
if __name__ == '__main__':
    app.run_server(debug=True)