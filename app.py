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

@app.route('/clientes')
def clientes():
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()
    cursor.execute(
        'SELECT * FROM customers'
    )
    lista_clientes = cursor.fetchall()

    cursor.close()
    connection.close()
    return render_template('clientes.html', alunos = lista_clientes)

@app.route ('/editar/<int:id>', methods = ['GET', 'POST'])
def editar_cliente(id):
    if request.method == 'POST':
        nome_aluno = request.form.get('nome_post')
        cpf_aluno = request.form.get('cpf_post')
        data_aluno = request.form.get('data_post')
        idade_aluno = request.form.get('idade_post')

        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()
        cursor.execute(
            'UPDATE customers SET name = ?, idade = ?, cpf = ?, dia = ? WHERE id = ?', 
            (nome_aluno, idade_aluno, cpf_aluno, data_aluno, id)
        ) 
        connection.commit()
        cursor.close()
        connection.close() 
        return redirect(url_for('clientes'))
    else:
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()
        cursor.execute(
            'SELECT * FROM customers WHERE id = ?',(id,)
            )
        id_cliente = cursor.fetchone()
        if id_cliente:
            cursor.close()
            connection.close()
            return render_template('edicao.html', cliente = id_cliente)
        else:
            return redirect(url_for('clientes'))
    
    # return f'essa é a pagina de ediçao do cliente de numero {id}'
           

    
if __name__ == '__main__':
    app.run(debug=True)