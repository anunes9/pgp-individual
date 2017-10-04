# !/usr/bin/python3
from flask import Flask, render_template, request, json
import csv
import os
import datetime

app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(APP_ROOT, 'static/db/database.csv')


@app.route("/", methods = ["GET"])
def main():
    return render_template('index.html', items=load_db(DATABASE)[1:])


@app.route("/loan", methods = ["POST"])
def loan():
    db = load_db(DATABASE)

    data = json.loads(request.data)

    new_loan = [str(len(db)), data["object"], data["name"], datetime.date.today().strftime("%d-%m-%Y"), "Loaned"]

    save_db(DATABASE, new_loan)

    return json.dumps({'status': 'OK', "data": new_loan})


@app.route("/return", methods= ["POST"])
def return_loan() :
    pass


def load_db(filename):
    with open(filename) as database:
        reader = csv.reader(database, delimiter=';')

        return [row for row in reader]


def save_db(filename, row):
    with open(filename, 'a') as database:
        writer = csv.writer(database, delimiter=';', lineterminator='\n')
        writer.writerow(row)


if __name__ == '__main__':
    app.run(debug=True)
