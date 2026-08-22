from flask import Flask, render_template, request
import csv
from pathlib import Path
import sqlite3

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome_aluno = request.form.get('nome_post')
        cpf_aluno = request.form.get('cpf_post')
        data_aluno = request.form.get('data_post')
        idade_aluno = request.form.get('idade_post')
        if nome_aluno == '':
            return render_template('index.html', erro = 'ERRO, o campo nome deve ser preenchido')
        elif cpf_aluno == '':
            return render_template('index.html', erro = 'ERRO, o campo cpf deve ser preenchido')
        elif data_aluno == '':
            return render_template('index.html', erro = 'ERRO, o campo data deve ser preenchido')
        elif idade_aluno == '':
            return render_template('index.html', erro = 'ERRO, o campo idade deve ser preenchido')
        else:
            print('---------ALUNO RECEBIDO---------')
            print(f'o nome do seu aluno é {nome_aluno} | o cpf é {cpf_aluno} |a idade é {idade_aluno} | e a data é {data_aluno}')
            print('---------------------------------')
            caminho_csv = Path(__file__).parent/'clientes.csv'
            with open(caminho_csv, 'a', newline='', encoding='utf-8') as arquivo:
                escritor = csv.writer(arquivo)
                escritor.writerow([nome_aluno, idade_aluno, cpf_aluno, data_aluno])

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)