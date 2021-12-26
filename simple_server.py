from flask import Flask
from flask import request
from flask import Response
from json import dumps
import logging

logging.basicConfig(filename='autotest.log', level=logging.DEBUG)

header = 'application/json'
app = Flask(__name__)


@app.route("/")
def status():
    data = {'message': 'hello world !'}
    return Response(dumps(data), status=200, mimetype=header)


@app.route("/echo", methods=["POST"])
def initilize():
    data = request.json
    return Response(dumps(data), status=201, mimetype=header)


app.run(debug=False, host='localhost', port=5003)
