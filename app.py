from os import getenv
from flask import Flask
from flask_httpauth import HTTPTokenAuth
from flask_cors import CORS

from util.configure import Configure
from util.helpers import respond_with

app = Flask(__name__)
auth = HTTPTokenAuth(scheme='Token')

CORS(app)
Configure(app, auth)


@app.route('/', methods=['GET'])
@auth.login_required
def index():
    """
    Dummy-index
    :return:
    """
    res = {'name': 'Flask API Boilerplate', 'version': '0.1.0'}
    return respond_with(res)


if __name__ == '__main__':
    app.run()
