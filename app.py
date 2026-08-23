from flask import Flask, render_template, request, redirect, url_for
import csv
from pathlib import Path
import sqlite3

app = Flask(__name__)

root_dir = Path(__file__).parent
db_file = root_dir / 'db' / 'db.sqlite3'

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
            connection = sqlite3.connect(db_file)
            cursor = connection.cursor()
            cursor.execute(
                'SELECT id FROM customers WHERE cpf = ?', (cpf_aluno,)
            )
            resultado = cursor.fetchone()
            if resultado :
                cursor.close()
                connection.close()
                return render_template('index.html', erro = 'ERRO, cliente ja cadastrado')
            else:
                cursor.execute(
                    'INSERT INTO customers'
                    '(id, name, idade, cpf, dia) '
                    'VALUES '
                    '(NULL, ?, ?, ?, ?)',
                    (nome_aluno, idade_aluno, cpf_aluno, data_aluno)
                            )
                connection.commit()
                print('---------ALUNO RECEBIDO---------')
                print(f'o nome do seu aluno é {nome_aluno} | o cpf é {cpf_aluno} |a idade é {idade_aluno} | e a data é {data_aluno}')
                print('---------------------------------')

                cursor.close()
                connection.close()
                return redirect(url_for('index'))
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(debug=True)