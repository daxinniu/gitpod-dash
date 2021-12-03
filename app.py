import dash
from dash import dcc
from dash import html
from dash import dash_table
from dash.dependencies import Input, Output
import dash_pivottable
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://bit.ly/elements-periodic-table')
def identity(x): return x

df2 = df.pivot_table(
    index='Period',
    columns='Group', 
    values='Element',
    aggfunc=identity,
)
df3 = pd.DataFrame(df2.to_records())

app = dash.Dash(__name__)


app.layout = html.Div([
    dcc.Dropdown(
        id="index-dropdown",
        options=[{'label': i, 'value': i} for i in df.columns],
        multi=False,
        value="Period"
    ),
    dcc.Dropdown(
        id="columns-dropdown",
        options=[{'label': i, 'value': i} for i in df.columns],
        multi=False,
        value="Group"
    ),
    dcc.Dropdown(
        id="values-dropdown",
        options=[{'label': i, 'value': i} for i in df.columns],
        multi=False,
        value="Element"
    ),
    dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df3.columns],
    data=df3.to_dict('records'),
    )
])

@app.callback([
    Output('table', 'data'),
    Output('table', 'columns')
    ], 
    [
        Input('index-dropdown', 'value'),
        Input('columns-dropdown', 'value'),
        Input('values-dropdown', 'value'),
    ])
def update_cols(index_val, columns_val, values_val):
    temp = df.pivot_table(
        index=index_val,
        columns=columns_val, 
        values=values_val,
        aggfunc=identity,
    )
    out_df = pd.DataFrame(temp.to_records())
    out_cols = [{"name": i, "id": i} for i in out_df]
    return out_df.to_dict('records'), out_cols

if __name__ == '__main__':
    app.run_server(debug=True)