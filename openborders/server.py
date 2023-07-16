from dash import Dash, html
import dash_ag_grid as dag
import pandas as pd

__all__ = [
    "serve_aggrid"
]


def serve_aggrid(df: pd.DataFrame, exclude=None):
    app = Dash(__name__)

    exclude = exclude or []

    columnDefs = [
        { 'field': c, 'sortable': True, 'filter': True} for c in df.columns if c not in exclude
    ]

    grid = dag.AgGrid(
        id="get-started-example-basic",
        rowData=df.to_dict("records"),
        columnDefs=columnDefs,
        className="ag-theme-material",
        columnSize="sizeToFit",
        dashGridOptions={
            'pagination' : True,
            
        }
    )

    app.layout = html.Div([grid])

    app.run()
