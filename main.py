import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'A API está no ar'

@app.route('/pegarvendas')
def pegarvendas():
    tabela = pd.read_csv('/Banco_de_Dados/banco-de-dados.csv')
    total_vendas = tabela['vendas'].sum()
    resposta = {'total_vendas': total_vendas}
    return jsonify(resposta)

# se você quiser roda no servidor da REPLS-REPLIT a platafomar pede para digitar o comando abaixo
app.run(host='0,0,0,0')

# se você for rodar na sua maquina basta colocar app.run() 