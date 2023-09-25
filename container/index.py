from flask import Flask, request
import os
from Operations import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    msg = os.environ['MESSAGE']
    ns = os.environ['NAMESPACE']
    o = Operations()
    return o.runningInfo(msg,ns)

@app.route("/_health")
def url_health():
    return "Running"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
