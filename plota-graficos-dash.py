# Importação das bibliotecas necessárias
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import numpy as np

# Criar dados simulados para abastecimento
np.random.seed(0)
datas = pd.date_range(start='2024-01-01', periods=30, freq='D')
litros_abastecidos = np.random.uniform(50, 200, size=30)  # Litros abastecidos
custo = np.random.uniform(100, 500, size=30)  # Custo do abastecimento

# Criar um DataFrame com os dados
df = pd.DataFrame({
    'Data': datas,
    'Litros': litros_abastecidos,
    'Custo': custo
})

# Inicializar o app Dash
app = dash.Dash(__name__)

# Layout do app
app.layout = html.Div([
    html.H1("Dashboard de Abastecimento"),
    dcc.Graph(
        id='grafico_litros',
        figure={
            'data': [
                go.Scatter(
                    x=df['Data'],
                    y=df['Litros'],
                    mode='lines+markers',
                    name='Litros Abastecidos'
                )
            ],
            'layout': go.Layout(
                title='Litros Abastecidos ao Longo do Tempo',
                xaxis={'title': 'Data'},
                yaxis={'title': 'Litros'}
            )
        }
    ),
    dcc.Graph(
        id='grafico_custo',
        figure={
            'data': [
                go.Bar(
                    x=df['Data'],
                    y=df['Custo'],
                    name='Custo do Abastecimento'
                )
            ],
            'layout': go.Layout(
                title='Custo do Abastecimento ao Longo do Tempo',
                xaxis={'title': 'Data'},
                yaxis={'title': 'Custo (R$)'}
            )
        }
    ),
    dcc.Graph(
        id='grafico_combined',
        figure={
            'data': [
                go.Scatter(
                    x=df['Data'],
                    y=df['Litros'],
                    mode='lines+markers',
                    name='Litros Abastecidos'
                ),
                go.Bar(
                    x=df['Data'],
                    y=df['Custo'],
                    name='Custo do Abastecimento',
                    yaxis='y2'
                )
            ],
            'layout': go.Layout(
                title='Litros e Custo de Abastecimento ao Longo do Tempo',
                xaxis={'title': 'Data'},
                yaxis={'title': 'Litros'},
                yaxis2={'title': 'Custo (R$)', 'overlaying': 'y', 'side': 'right'}
            )
        }
    )
])

# Executar o app
if __name__ == '__main__':
    app.run_server(debug=True)
