from altair import Chart, Tooltip
from pandas import DataFrame


def chart(df: DataFrame, x: str, y: str, target: str) -> Chart:
    '''
    Creates a chart object to be displayed in the view page. 
    '''
    graph = Chart(df,
    title=f"{y} by {x} for {target}"
    ).mark_circle(size=100).encode(x=x,
                                y=y,
                                color=target,
                                tooltip=Tooltip(df.columns.to_list()
                                )).properties(height=250,
                                            width=1000,
                                            padding=5,
                                            background='white')


    return graph

