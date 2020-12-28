from flask import Flask
from flask import render_template
import requests
from requests.auth import HTTPBasicAuth
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/embed-auth')
def auth():
    response = requests.get(
        'https://www.daloopa.com/api/v1/embed/token',
        auth=HTTPBasicAuth(
            'jeremy@daloopa.com',
            '8sY2XViCw7zneBm-InZPS4x8iJ18BIytwtfNKFq3BNZZAlIH1PjYeA'
        ),
    )

    return json.loads(response.text)

@app.route('/')
def index():
    return render_template("index.html")
