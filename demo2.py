from flask import Flask

import requests
import json

app = Flask(__name__)

@app.route('/')
def demo():
    """Create some jokes on demo.plone.org"""
    url = 'https://demo.plone.org/en/demo'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    auth = ('editor', 'editor')
    jokes = random_jokes()
    for data in jokes:
        joke = data['joke']
        if len(joke) > 40:
            joke_title = joke[:37] + '...'
        else:
            joke_title = joke

        payload = {
            '@type': 'Document',
            'title': joke_title,
            'description': joke,
            'id': str(data['id']),
        }
        response = requests.post(
            url,
            headers=headers,
            json=payload,
            auth=auth,
        )
        response.raise_for_status()
        app.logger.info(f'Created joke {response.json()["@id"]}')
    return f'Created {len(jokes)} jokes'


def random_jokes(amount=2):
    jokes = requests.get(f'http://api.icndb.com/jokes/random/{amount}?escape=javascript')
    jokes.raise_for_status()
    return json.loads(jokes.text)['value']
