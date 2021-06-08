from flask import Flask, request
from werkzeug.routing import Rule

app = Flask(__name__)

app.url_map.add(Rule('/', endpoint=''))

@app.endpoint('')
def hello_world():
    return 'METHOD: ' + request.method
