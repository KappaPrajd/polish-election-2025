import requests
import json

def get_odds():
    response = requests.get('https://production-superbet-offer-pl.freetls.fastly.net/v2/pl-PL/events/7986075')

    response_json = json.loads(response.content)
    data = response_json['data'][0]['odds']

    trzaskowski_odds = next((odds for odds in data if odds['specialBetValue'] == 'Rafał Trzaskowski'))['price']
    nawrocki_odds = next((odds for odds in data if odds['specialBetValue'] == 'Karol Nawrocki'))['price']

    return {
        'bookmaker': 'Superbet',
        'trzaskowski': float(trzaskowski_odds),
        'nawrocki': float(nawrocki_odds)
    }