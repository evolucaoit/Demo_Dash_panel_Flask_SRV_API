# api.py

from flask import Flask, jsonify
import numpy as np
import pandas as pd

app = Flask(__name__)

@app.route('/dados', methods=['GET'])
def obter_dados():
    # Dados simulados
    np.random.seed(0)
    cidades = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador', 'Fortaleza', 'Brasília', 'Curitiba', 'Manaus', 'Recife', 'Porto Alegre']
    populacoes = np.random.randint(1_000_000, 12_000_000, size=len(cidades))
    rendas = np.random.uniform(2000, 10000, size=len(cidades))
    
    dados = {
        'cidades': cidades,
        'populacoes': populacoes.tolist(),
        'rendas': rendas.tolist()
    }
    
    return jsonify(dados)

if __name__ == '__main__':
    app.run(port=8888)
