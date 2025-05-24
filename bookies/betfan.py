import requests
import json

def get_odds():
    response = requests.get('https://betfan.pl/api/v1/market/events/29455489?sportId=2285')

    response_json = json.loads(response.content)
    
    data = response_json['data']['event']['games'][0]['outcomes']

    trzaskowski_odds = next((odds for odds in data if odds['outcomeName'] == 'Rafał Trzaskowski'))['outcomeOdds']
    nawrocki_odds = next((odds for odds in data if odds['outcomeName'] == 'Karol Nawrocki'))['outcomeOdds']

    return {
        'bookmaker': 'Betfan',
        'trzaskowski': float(trzaskowski_odds),
        'nawrocki': float(nawrocki_odds)
    }