import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
from dash import Dash, dcc, html, Input, Output

df = [dict(Task="Job-1", Start='2017-01-01', Finish='2017-02-02', Proyecto="Proyecto 1", Avance=100),
      dict(Task="Job-1", Start='2017-02-15', Finish='2017-03-15', Proyecto="Proyecto 1", Avance=20),
      dict(Task="Job-2", Start='2017-01-17', Finish='2017-02-17', Proyecto="Proyecto 1", Avance=0),
      dict(Task="Job-2", Start='2017-01-17', Finish='2017-02-17', Proyecto="Proyecto 1", Avance=100),
      dict(Task="Job-3", Start='2017-03-10', Finish='2017-03-20', Proyecto="Proyecto 1", Avance=0),
      dict(Task="Job-3", Start='2017-04-01', Finish='2017-04-20', Proyecto="Proyecto 1", Avance=0),
      dict(Task="Job-3", Start='2017-05-18', Finish='2017-06-18', Proyecto="Proyecto 1", Avance=60),
      dict(Task="Job-4", Start='2017-01-14', Finish='2017-03-14', Proyecto="Proyecto 1", Avance=100)]

fig = ff.create_gantt(df, colors='Cividis', index_col='Avance', group_tasks=True, title='Gantt General')

# Actualiza el formato y estilo del eje Y
fig.update_layout(yaxis=dict(categoryarray=["Proyecto 1", "Job-1", "Job-2", "Job-3", "Job-4"], type="category"))

# Crea la aplicación Dash
app = Dash(__name__)

# Define el diseño de la aplicación
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

# Ejecuta la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)

