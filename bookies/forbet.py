import requests
import json

def get_odds():
    response = requests.get('https://www.iforbet.pl/rest/market/events/44836095')

    response_json = json.loads(response.content)
    data = response_json['data']['eventGames'][0]['outcomes']

    trzaskowski_odds = next((odds for odds in data if odds['outcomeName'] == 'Rafał Trzaskowski'))['outcomeOdds']
    nawrocki_odds = next((odds for odds in data if odds['outcomeName'] == 'Karol Nawrocki'))['outcomeOdds']

    return {
        'bookmaker': 'Forbet',
        'trzaskowski': float(trzaskowski_odds),
        'nawrocki': float(nawrocki_odds)
    }