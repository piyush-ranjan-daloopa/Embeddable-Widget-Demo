## Demo Project for Daloopa Embed Widget

### Pre-requisites

Make sure you have python 3.6 or above installed. 

### Installing the dependencies

```
pip install -r requirements.txt
```

### Starting a flask server

```
EXPORT FLASK_APP=run.py

flask run
```

## Getting Started

Step 1: 

Assuming your local server runs at localhost:5000, let’s embed our widget on the home page at route localhost:5000/index. 

```html
<html>
    <body>
        <div id='daloopa-embed' style="height:500px;width: 500px" data-src-id="998198">
            <!-- Embed.bundle.js initializes the DaloopaWidget object on the window object. -->
            <script src='https://www.daloopa.com/static/embed.bundle.js'></script>

            <script>
                if (window.DaloopaWidget) {
                    // Here we add a javascript function to fetch a token from your own server.
                    // The function should return a Promise that resolves to a token string.
                    window.DaloopaWidget.addFetchTokenFn(() => {
                        return fetch('/embed-auth')
                                .then((response) => response.json())
                                .then((payload) => payload.token);
                    });

                    // And then we render the widget.
                    window.DaloopaWidget.render();
                }
            </script>
        </div>
    </body>
</html>
```

Step 2: 

Handles authentication token on your server. In this example, the example flask server handles the routes with the following: 

```python
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
    # a Daloopa Embed Token, whose response looks like this:
    #
    # response = {
    #   exp: <expiration_time_in_ms_since_epoch>,
    #   token: <token_string>,
    # }
    response = requests.get(
        'https://www.daloopa.com/api/v1/embed/token',
        auth=HTTPBasicAuth(
            # Your username
            '<username>',
            # Your Daloopa API key. Please put the key in a secure and private place.
            '<api-key>'
        ),
    )

    return json.loads(response.text)

@app.route('/')
def index():
    return render_template("index.html")
```

## Open a browser and go to this URL: `http://localhost:5000`

You should see the widget getting rendered correctly.

## Contact us

Please feel free to reach out to us via Github Issues or Github Discussions.

