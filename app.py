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
temp = df.values.tolist()
temp.insert(0, df.columns.tolist())
app = dash.Dash(__name__)
server = app.server

#import pdb; pdb.set_trace()
app.layout = html.Div(
    dash_pivottable.PivotTable(
        data=temp,
        cols=['Element'],
        #rows=["Location"],
        vals=["AtomicMass"]
    )
)

if __name__ == "__main__":
    app.run_server(debug=True)