#/usr/bin/python3
from flask import Flask, render_template, request, json

app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route("/", methods = ["GET", "POST"])
def main():
    return render_template('index.html')

@app.route("/loan", methods = ["POST"])
def loan():
    print(json.loads(request.data)["object"])
    print("chegou")
    return json.dumps({'status':'OK', "data":request.json});

if __name__ == '__main__':
    app.run(debug=True)