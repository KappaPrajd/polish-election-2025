import requests
import json

def get_odds():
    # these are not secrets, obtained by inspecting dev tools of sts website
    headers = {
        "x-api-key": "5ZU3zqUqo8WjprFgAM",
        "x-request-uuid": "0ddc9d7c-1c9b-4e56-ade2-91cd31a73b87"
    }

    trzaskowski_response = requests.get('https://api.sts.pl/web/v1/offer/prematch/720678171', headers=headers)
    nawrocki_response = requests.get('https://api.sts.pl/web/v1/offer/prematch/720678177', headers=headers)

    trzaskowski_json = json.loads(trzaskowski_response.content)
    nawrocki_json = json.loads(nawrocki_response.content)

    trzaskowski_odds = trzaskowski_json['markets'][0]['odds'][0]['value']
    nawrocki_odds = nawrocki_json['markets'][0]['odds'][0]['value']

    return {
        'bookmaker': 'STS',
        'trzaskowski': float(trzaskowski_odds),
        'nawrocki': float(nawrocki_odds)
    }
