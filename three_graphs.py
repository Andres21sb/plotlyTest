from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Sample data
df1 = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 11, 12, 13, 14]
})

df2 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 22]
})

df3 = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Value': [8, 15, 10, 7, 12]
})

# Initialize the Dash app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    dcc.Graph(id='graph-1'),
    dcc.Dropdown(
        id='dropdown-2',
        options=[
            {'label': name, 'value': name} for name in df2['Name']
        ],
        value='Alice',
        multi=False
    ),
    dcc.Graph(id='graph-3'),
])

# Callback to update the first graph based on the slider value
@app.callback(
    Output('graph-1', 'figure'),
    [Input('slider-1', 'value')]
)
def update_graph1(selected_value):
    filtered_df1 = df1[df1['x'] <= selected_value]
    fig1 = px.scatter(filtered_df1, x='x', y='y', title=f'Scatter Plot (x <= {selected_value})')
    return fig1

# Callback to update the second graph based on the dropdown selection
@app.callback(
    Output('graph-2', 'figure'),
    [Input('dropdown-2', 'value')]
)
def update_graph2(selected_name):
    filtered_df2 = df2[df2['Name'] == selected_name]
    fig2 = px.bar(filtered_df2, x='Name', y='Age', title=f'Bar Graph for {selected_name}')
    return fig2

# Callback to update the third graph based on the radio button selection
@app.callback(
    Output('graph-3', 'figure'),
    [Input('radio-3', 'value')]
)
def update_graph3(selected_category):
    filtered_df3 = df3[df3['Category'] == selected_category]
    fig3 = px.bar(filtered_df3, x='Category', y='Value', title=f'Bar Graph for Category {selected_category}')
    return fig3

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
