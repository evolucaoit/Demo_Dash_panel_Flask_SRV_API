# Demo_Dash_panel_Flask_SRV_API 🚀📊

Bem-vindo ao repositório **Demo_Dash_panel_Flask_SRV_API**! Este projeto demonstra como construir painéis e dashboards dinâmicos utilizando a biblioteca Dash do Python, servindo dados através de uma API Flask. Aqui, você encontrará exemplos práticos e detalhados de como integrar essas tecnologias para criar visualizações interativas e informativas.

## 🚀 Visão Geral

Este repositório foi criado para fornecer um exemplo funcional de como combinar o **Dash** com o **Flask** para gerar gráficos dinâmicos e dashboards. O objetivo é mostrar a facilidade de criar aplicações web interativas e flexíveis, utilizando **Python** e suas poderosas bibliotecas para visualização de dados.

# Demo_Dash_panel_Flask_SRV_API 🚀📊

Bem-vindo ao **Demo_Dash_panel_Flask_SRV_API**! Neste repositório, você encontrará exemplos completos de como construir dashboards dinâmicos e gráficos avançados usando **Dash**, **Flask**, e **Seaborn**. Este projeto demonstra a integração entre uma API Flask e um painel Dash para visualização de dados interativos.

## 🎯 Visão Geral

Este repositório contém exemplos práticos de como construir gráficos e dashboards utilizando **Dash** e **Flask**. A combinação dessas tecnologias permite criar visualizações de dados interativas que são atualizadas em tempo real, proporcionando uma visão clara e detalhada dos dados.

## 🛠️ Estrutura do Projeto

Aqui está um resumo da estrutura do repositório:

- **`teste-api-serve-dados-flask-para-dash.py`**: Código exemplo para servir dados via API Flask.
- **`plota-graficos-dash.py`**: Código para gerar gráficos básicos com Dash.
- **`plota-graficos-dash-melhorado.py`**: Versão aprimorada do código de gráficos com Dash.
- **`dashboard-dash-plota-graficos-via-dados-api.py`**: Código para criar um dashboard completo utilizando dados da API Flask.

## 📸 Exemplos de Gráficos

### Gráfico Avançado do Dashboard

Aqui está um exemplo de um gráfico avançado no dashboard, exibindo múltiplas visualizações em um layout estilizado:

![Dashboard Avançado](https://github.com/evolucaoit/Demo_Dash_panel_Flask_SRV_API/blob/main/screencapture-127-0-0-1-8050-2024-08-27-10_21_18.png?raw=true)

### Gráfico de Controle de Abastecimento

Um exemplo de gráfico de controle de abastecimento que mostra dados de forma clara e visual:

![Gráfico de Controle de Abastecimento](https://github.com/evolucaoit/Demo_Dash_panel_Flask_SRV_API/blob/main/screencapture-127-0-0-1-8050-2024-08-27-10_19_43.png?raw=true)

### Gráfico de Barras

Um exemplo de gráfico de barras para visualização de dados quantitativos:

![Gráfico de Barras](https://github.com/evolucaoit/Demo_Dash_panel_Flask_SRV_API/blob/main/newplot.png?raw=true)

### Gráfico de Pizza

Um exemplo de gráfico de pizza para visualização de distribuições percentuais:

![Gráfico de Pizza](https://github.com/evolucaoit/Demo_Dash_panel_Flask_SRV_API/blob/main/newplot%20(1).png?raw=true)

## 📝 Exemplo de Código

Aqui está um exemplo simplificado da lógica usada para gerar gráficos dinâmicos com Dash e Flask:

```python
# Importação das bibliotecas necessárias
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import numpy as np

# Dados reais fictícios de cidades do Brasil
np.random.seed(0)
cidades = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador', 'Fortaleza', 'Brasília', 'Curitiba', 'Manaus', 'Recife', 'Porto Alegre']
populacoes = np.random.randint(1_000_000, 12_000_000, size=len(cidades))
rendas = np.random.uniform(2000, 10000, size=len(cidades))

# Criar um DataFrame com os dados
df = pd.DataFrame({
    'Cidade': cidades,
    'População': populacoes,
    'Renda Média': rendas
})

# Inicializar o app Dash
app = dash.Dash(__name__)

# Layout do app com tema escuro
app.layout = html.Div(style={'backgroundColor': '#333', 'color': '#FFF', 'padding': '20px'}, children=[
    html.H1("Dashboard de Cidades do Brasil 🌟", style={'textAlign': 'center', 'color': '#00CFFF'}),
    html.Div(style={'display': 'flex', 'justifyContent': 'space-around'}, children=[
        dcc.Graph(
            id='grafico_populacao',
            figure={
                'data': [
                    go.Bar(
                        x=df['Cidade'],
                        y=df['População'],
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
                        labels=df['Cidade'],
                        values=df['Renda Média'],
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
                    x=df['Cidade'],
                    y=df['População'],
                    mode='markers+lines',
                    name='População',
                    marker={'color': '#00CFFF', 'size': 10}
                ),
                go.Scatter(
                    x=df['Cidade'],
                    y=df['Renda Média'],
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
```

### 📋 O que você encontrará aqui:

- **Código de exemplo**: Implementações básicas para criar gráficos e dashboards.
- **API Flask**: Servindo dados para o Dash através de uma API RESTful.
- **Exemplos de gráficos**: Utilizando a biblioteca Seaborn para visualizações avançadas.
- **Documentação**: Instruções detalhadas sobre como configurar e utilizar o projeto.

## 📁 Estrutura do Repositório

```plaintext
Demo_Dash_panel_Flask_SRV_API/
│
├── app/
│   ├── __init__.py        # Inicializa o aplicativo Flask
│   ├── api.py             # Define a API Flask
│   └── data.py            # Funções para geração de dados
│
├── dash_app/
│   ├── __init__.py        # Inicializa o aplicativo Dash
│   └── layout.py          # Define o layout do dashboard
│
├── requirements.txt       # Dependências do projeto
├── run_flask.py           # Script para rodar a API Flask
├── run_dash.py            # Script para rodar o aplicativo Dash
└── README.md              # Este arquivo

```

