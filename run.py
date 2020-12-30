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
    # Authenticate the user here if needed.

    # Once the user is authenticated, you can request for
    # a Daloopa Embed Token, which looks like this:
    #
    # response = {
    #   exp: <expiration_time_in_ms_since_epoch>,
    #   token: <token_string>,
    # }
    response = requests.get(
        'https://www.daloopa.com/api/v1/embed/token',
        auth=HTTPBasicAuth(
            # Your username
            '<your-user-name>',
            # Your Daloopa API key. Please put the key in a secure and private storage.
            '<your-api-key>'
        ),
    )

    return json.loads(response.text)

@app.route('/')
def index():
    return render_template("index.html")
