from dash import Dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Sample data
df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 11, 12, 13, 14]
})

# Initialize the Dash app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    dcc.Graph(id='scatter-plot'),
    dcc.Slider(
        id='slider',
        min=1,
        max=5,
        step=1,
        marks={i: str(i) for i in range(1, 6)},
        value=3
    )
])

# Callback to update the graph in response to slider changes
@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('slider', 'value')]
)
def update_graph(selected_value):
    filtered_df = df[df['x'] <= selected_value]
    fig = px.scatter(filtered_df, x='x', y='y', title=f'Scatter Plot (x <= {selected_value})')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
