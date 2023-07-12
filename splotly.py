import base64
import io
import plotly.figure_factory as ff
import plotly.graph_objects as go 
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

df = [dict(Proyecto="Proyecto 1", Inicio='2023-01-01', Final='2023-06-02', Avance=100),
      dict(Proyecto="Proyecto 2", Inicio='2023-02-15', Final='2023-09-15', Avance=80),
      dict(Proyecto="Proyecto 3", Inicio='2023-01-17', Final='2023-05-17', Avance=100),
      dict(Proyecto="Proyecto 4", Inicio='2023-01-17', Final='2023-02-17', Avance=100),
      dict(Proyecto="Proyecto 5", Inicio='2023-08-10', Final='2023-12-20', Avance=0),
      dict(Proyecto="Proyecto 6", Inicio='2023-08-01', Final='2023-12-20', Avance=0),
      dict(Proyecto="Proyecto 7", Inicio='2023-05-18', Final='2023-08-18', Avance=60),
      dict(Proyecto="Proyecto 8", Inicio='2023-01-14', Final='2023-03-14', Avance=100)]

#colors = {'Sin iniciar': 'rgb(220, 0, 0)', 'En progreso': 'rgb(255, 255, 0)','Completado': 'rgb(0, 255, 100)'}
fig = px.timeline(df, x_start="Inicio", x_end="Final", y="Proyecto", color="Avance")
#fig = ff.create_gantt(df, colors='Cividis', index_col='Avance',  show_colorbar=True,
#                      group_tasks=True, title='Gantt General')
fig.update_layout(paper_bgcolor="rgba(0,0,0,0)")

 

app = Dash(external_stylesheets=[dbc.themes.MORPH, dbc.icons.FONT_AWESOME])

app.layout = html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Button('Cargar archivo Excel')
    ),
    html.Div(id='output-data'),
    dcc.Graph(id='graph1',figure=fig)
])

def parse_excel(contents, filename):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    try:
        # Lee el archivo Excel como DataFrame
        df = pd.read_excel(io.BytesIO(decoded))
        return html.Div([
            html.H5(f'Archivo subido: {filename}'),
            html.Hr(),
            #html.P(f'Contenido del DataFrame: {df.to_string()}')
        ])
    except Exception as e:
        return html.Div([
            'Ocurrió un error al procesar el archivo.'
        ])

# Define la callback para procesar la carga del archivo
@app.callback(Output('output-data', 'children'),
              Output('graph1','figure'),
              Input('upload-data', 'contents'),
              Input('upload-data', 'filename'))
def update_output(contents, filename):
    if contents is not None:
        decoded = base64.b64decode(contents.split(',')[1])
        try:
            # Lee el archivo Excel como DataFrame
            df = pd.read_excel(io.BytesIO(decoded))
            fig1 = px.timeline(df, x_start="Inicio", x_end="Final", y="Proyecto", color="Avance")
            fig1.update_layout(paper_bgcolor="rgba(0,0,0,0)")

        except Exception as e:
            print('error: ',e)
        
        return parse_excel(contents, filename) ,fig1
    else:
        return '' ,fig

app.run_server(debug=True)