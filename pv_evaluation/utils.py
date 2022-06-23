import pandas as pd
import itertools
import plotly.graph_objects as go


def compare_plots(*figs):
    """Combine plotly graphs into one, changing color as necessary."""

    combined = go.Figure()
    for i, fig in enumerate(figs):
        fig.update_traces(marker=dict(color=i), showlegend=True)
        if fig.data[0].name == "":
            fig.update_traces(name=i)
        combined.add_traces(fig.data)

        combined.update_xaxes(range=fig.layout.xaxis.range)
        combined.update_yaxes(range=fig.layout.yaxis.range)

    return combined


def expand_grid(**kwargs):
    """Get all value combinations.
    """
    return pd.DataFrame.from_records(itertools.product(*kwargs.values()), columns=kwargs.keys())
