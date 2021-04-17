from flask import Flask

import requests
import json

app = Flask(__name__)

@app.route('/')
def demo():
    data = random_joke()
    return data['joke']


def random_joke():
    response = requests.get('http://api.icndb.com/jokes/random?escape=javascript')
    response.raise_for_status()
    return json.loads(response.text)['value']
