from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/<path:path>', methods=['GET'])
def static_proxy(path):
  return send_from_directory('dist', path)


@app.route('/')
def root():
  return send_from_directory('dist', 'index.html')
