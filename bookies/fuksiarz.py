import requests
import json

def get_odds():
    response = requests.get('https://fuksiarz.pl/rest/market/events/16032613')

    response_json = json.loads(response.content)
    
    data = response_json['data']['eventGames'][0]['outcomes']

    trzaskowski_odds = next((odds for odds in data if odds['outcomeName'] == 'Rafał Trzaskowski'))['outcomeOdds']
    nawrocki_odds = next((odds for odds in data if odds['outcomeName'] == 'Karol Nawrocki'))['outcomeOdds']

    return {
        'bookmaker': 'Fuksiarz',
        'trzaskowski': float(trzaskowski_odds),
        'nawrocki': float(nawrocki_odds)
    }