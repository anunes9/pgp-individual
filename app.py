# -*- coding: utf-8 -*-
# !/usr/bin/python3

from flask import Flask, render_template, request, json, abort
import csv
import os
import datetime

app = Flask(__name__)

# Fazer refresh cada vez que ha uma alteracao no servidor
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Referencia para o diretorio do servidor
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
# Referencia para o ficheiro da base de dados
DATABASE = os.path.join(APP_ROOT, 'static/db/database.csv')


# Rota principal do servidor
@app.route("/", methods=["GET"])
def main():
    """
    Funcao principal que faz render a pagina inicial

    :return: render da pagina inicial
    """
    return render_template('index.html', items=load_db(DATABASE)[1:])


# Rota para receber um emprestimo
@app.route("/loan", methods=["POST"])
def loan():
    """
    Funcao que recebe um pedido POST de um novo emprestimo

    :return: a informacao sobre o novo emprestimo
    """
    db = load_db(DATABASE)

    data = json.loads(request.data)

    new_loan = [str(len(db)), data["object"], data["name"], datetime.date.today().strftime("%d-%m-%Y"), "Loaned"]

    db.append(new_loan)

    save_db(DATABASE, db)

    return json.dumps({'status': 'OK', "data": new_loan})


# Rota para receber uma devolucao
@app.route("/return_loan", methods=["POST"])
def return_loan():
    """
    Funcao que recebe um pedido POST de uma devolucao de um emprestimo

    :return: OK se a devolucao for bem sucedida, NOK caso contrario
    """
    db = load_db(DATABASE)

    data = json.loads(request.data)

    id = int(data["id"])

    if db[id][4] == "Returned":
        status = 'NOK'
    else:
        save_db(DATABASE, db)
        db[id][4] = "Returned"
        status = 'OK'

    return json.dumps({'status': status, 'data': 'OK'})


def load_db(filename):
    """
    Funcao que le a base de dados de um ficheiro csv para uma lista de listas

    :param filename: nome do ficheiro csv da base de dados
    :return: lista de listas com a informacao da base de dados
    """
    with open(filename) as database:
        reader = csv.reader(database, delimiter=';')

        return [row for row in reader]


def save_db(filename, db):
    """
    Funcao que guarda a base de dados para um ficheiro csv

    :param filename: nome do ficheiro csv da base de dados
    :param db: lista de listas com a informacao da base de dados para guardar
    """
    with open(filename, 'w') as database:
        writer = csv.writer(database, delimiter=';', lineterminator='\n')
        for row in db:
            writer.writerow(row)


if __name__ == '__main__':
    app.run(debug=True)
