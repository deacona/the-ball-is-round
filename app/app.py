import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
import plotly.graph_objects as go

import src.utilities as utilities

data = utilities.get_master("quality")
overall_score = data.score.mean()
# range_max = data.score.max()

data_pivot = pd.pivot_table(
    data,
    values="score",
    index="file",
    columns="category",
    aggfunc=np.mean,
    margins=False,
)
# print(data_pivot)

fig = go.Figure(
    data=go.Heatmap(
        z=data_pivot.values,
        x=data_pivot.columns,
        y=data_pivot.index,
        colorscale="Viridis",
        colorbar=dict(title="<b>Average Score</b>"),
    )
)

fig.update_layout(
    # title='Average Score by Category and File',
    xaxis=dict(title="<b>Category</b>"),
    yaxis=dict(title="<b>File</b>", autorange="reversed"),
)

fig.update_xaxes(side="top")

# fig.write_image("assets/dashboard.png")

app = dash.Dash(__name__)
app.title = "Data Quality Dashboard"

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.H1(children="Data Quality Dashboard", className="header-title"),
                html.P(
                    children="Various data quality metrics"
                    " aggregated by category and file."
                    " Overall score is {0:.2f}.".format(overall_score),
                    className="header-description",
                ),
            ],
            className="header",
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(id="score_heatmap", figure=fig),
                    className="card",
                ),
            ],
            className="wrapper",
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
