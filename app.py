# !/usr/bin/python3
from flask import Flask, render_template, request, json
import csv
import os
import datetime

app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(APP_ROOT, 'static/db/database.csv')

# date format yyyy-mm-dd


@app.route("/", methods = ["GET", "POST"])
def main():
    return render_template('index.html')


@app.route("/loan", methods = ["POST"])
def loan():
    db = load_db(DATABASE)
    data = json.loads(request.data)
    # datetime.date.today() 2017-10-03
    new_loan = [str(len(db)), data["object"], data["name"], datetime.date.today().strftime("%d-%m-%Y"), "Loaned"]
    print("new loan" , new_loan)
      # list of lists
    db.append(new_loan)
    print("DB", db)
    return json.dumps({'status': 'OK', "data": db[1:]})


def load_db(filename):
    with open(filename) as database:
        reader = csv.reader(database, delimiter=';')

        return [row for row in reader]


def save_db(db):
    pass


if __name__ == '__main__':
    app.run(debug=True)
