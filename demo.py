from flask import Flask

import requests
import json

app = Flask(__name__)

@app.route('/')
def demo():
    data = random_joke()
    return data['joke']


def random_joke():
    joke = requests.get('http://api.icndb.com/jokes/random?escape=javascript')
    return json.loads(joke.text)['value']
