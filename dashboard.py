import plotly.express as px

def create_chart(df, plan):
    chart_type = plan["chart"]
    x = plan["x"]
    y = plan["y"]
    agg = plan["aggregation"]
    title = plan["title"]

    if agg:
        df = df.groupby(x)[y].agg(agg).reset_index()

    if chart_type == "bar":
        fig = px.bar(df, x=x, y=y, title=title)

    elif chart_type == "line":
        fig = px.line(df, x=x, y=y, title=title)

    elif chart_type == "histogram":
        fig = px.histogram(df, x=x, title=title)

    elif chart_type == "pie":
        fig = px.pie(df, names=x, values=y, title=title)

    else:
        raise ValueError("Unsupported chart type")

    return fig
