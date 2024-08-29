# dash_app.py

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import requests

# Inicializar o app Dash
app = dash.Dash(__name__)

# Função para obter dados da API Flask
def obter_dados():
    url = 'http://127.0.0.1:8888/dados'
    resposta = requests.get(url)
    dados = resposta.json()
    return dados

# Obter os dados
dados = obter_dados()
cidades = dados['cidades']
populacoes = dados['populacoes']
rendas = dados['rendas']

# Layout do app com tema escuro
app.layout = html.Div(style={'backgroundColor': '#333', 'color': '#FFF', 'padding': '20px'}, children=[
    html.H1("Dashboard de Cidades do Brasil 🌟", style={'textAlign': 'center', 'color': '#00CFFF'}),
    html.Div(style={'display': 'flex', 'justifyContent': 'space-around'}, children=[
        dcc.Graph(
            id='grafico_populacao',
            figure={
                'data': [
                    go.Bar(
                        x=cidades,
                        y=populacoes,
                        marker={'color': '#FF5733'}
                    )
                ],
                'layout': go.Layout(
                    title='População das Cidades 📊',
                    xaxis={'title': 'Cidade'},
                    yaxis={'title': 'População'},
                    plot_bgcolor='#333',
                    paper_bgcolor='#333',
                    font={'color': '#FFF'}
                )
            }
        ),
        dcc.Graph(
            id='grafico_renda',
            figure={
                'data': [
                    go.Pie(
                        labels=cidades,
                        values=rendas,
                        hole=0.4,
                        marker={'colors': ['#FFC300', '#FF5733', '#DAF7A6', '#581845', '#FF0000', '#C70039', '#900C3F', '#1C2833', '#2E86C1', '#45B39D']}
                    )
                ],
                'layout': go.Layout(
                    title='Distribuição da Renda Média 💰',
                    plot_bgcolor='#333',
                    paper_bgcolor='#333',
                    font={'color': '#FFF'}
                )
            }
        )
    ]),
    dcc.Graph(
        id='grafico_combined',
        figure={
            'data': [
                go.Scatter(
                    x=cidades,
                    y=populacoes,
                    mode='markers+lines',
                    name='População',
                    marker={'color': '#00CFFF', 'size': 10}
                ),
                go.Scatter(
                    x=cidades,
                    y=rendas,
                    mode='markers+lines',
                    name='Renda Média',
                    yaxis='y2',
                    marker={'color': '#FF5733', 'size': 10}
                )
            ],
            'layout': go.Layout(
                title='População e Renda Média das Cidades 📉',
                xaxis={'title': 'Cidade'},
                yaxis={'title': 'População', 'side': 'left'},
                yaxis2={'title': 'Renda Média (R$)', 'overlaying': 'y', 'side': 'right'},
                plot_bgcolor='#333',
                paper_bgcolor='#333',
                font={'color': '#FFF'}
            )
        }
    ),
    html.Div([
        html.P("🔍 Explore a visualização dos dados com gráficos interativos.", style={'textAlign': 'center'}),
        html.P("📈 Gráficos de População e Renda Média das principais cidades do Brasil.", style={'textAlign': 'center'})
    ], style={'textAlign': 'center', 'marginTop': '20px'})
])

# Executar o app
if __name__ == '__main__':
    app.run_server(debug=True)
