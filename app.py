import pandas as pd
import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go

data = pd.read_csv('Public_School_Locations_2018-19.csv')
Data = pd.DataFrame(data)

mapbox_access_token = "pk.eyJ1Ijoid2FkZTEyOSIsImEiOiJja2Q0bW1pYXkxaWszMnFtdHpyNGh6MHBjIn0.T7KO_vcHJuW40biVeCIUGQ"

fig = go.Figure(go.Scattermapbox(
    lat=Data['LAT'],
    lon=Data['LON'],
    mode='markers',
    marker=go.scattermapbox.Marker(
        size=3.5,
        color=Data['OBJECTID'],
        # opacity=0.3
    ),
    text=Data['NAME'],
))

fig.update_layout(
    title=dict(
        text='Public Schools in the United States',
        x=.5,
    ), autosize=True,
    hovermode='closest',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=38,
            lon=-95
        ),
        style='streets',
        pitch=0,
        zoom=3.5
    ),
    height=600,
    margin={"r": 20, "t": 50, "l": 20, "b": 0}
)



app = dash.Dash()
app.layout = html.Div([
    html.Div(dcc.Graph(figure=fig))
])

app.run_server(debug=True, use_reloader=False)
