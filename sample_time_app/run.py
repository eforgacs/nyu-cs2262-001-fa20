from datetime import datetime

from flask import Flask

app = Flask(__name__)


@app.route('/time')
def hello_world():
    now = datetime.now()
    return now.strftime("%H:%M:%S")


app.run(host='127.0.0.1',
        port=8080,
        debug=True)
