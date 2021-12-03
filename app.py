import dash
import dash_html_components as html
import dash_pivottable
import pandas as pd
from dash import dash_table

df = pd.read_csv('https://bit.ly/elements-periodic-table')
def identity(x): return x
df2 = df.pivot_table(
            index='Period',
            columns='Group', 
            values='Element',
            aggfunc=identity,
        )

app = dash.Dash(__name__)
server = app.server


app.layout = html.Div(
    dash_pivottable.PivotTable(
        data=[
            ['Animal', 'Count', 'Location'],
            ['Zebra', 5, 'SF Zoo'],
            ['Tiger', 3, 'SF Zoo'],
            ['Zebra', 2, 'LA Zoo'],
            ['Tiger', 4, 'LA Zoo'],
        ],
        cols=["Animal"],
        rows=["Location"],
        vals=["Count"]
    )
)

if __name__ == "__main__":
    app.run_server(debug=True)