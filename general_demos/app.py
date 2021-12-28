from flask import Flask
from flask import request
from flask import Response
from json import dumps, loads
import logging

logging.basicConfig(filename='autotest.log', level=logging.DEBUG)

header = 'application/json'
app = Flask(__name__)


@app.route("/", methods=['GET'])
def status():
    data = {'message': 'hello world !'}
    return Response(dumps(data), status=200, mimetype=header)


@app.route("/echo", methods=["POST"])
def initilize():
    data = request.json
    return Response(dumps(data), status=201, mimetype=header)


if __name__ == "__main__":
    app.run(debug=False, host='localhost')  # , port=5003)
    # run with  py -m flask run --port 5003
