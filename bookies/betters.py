import requests
import json

def get_odds():
    response = requests.get('https://offer.lvbet.pl/client-api/v5/markets/search/?matches_ids=m:1730905381.5473998')

    response_json = json.loads(response.content)
    
    data = response_json[0]['selections']

    trzaskowski_odds = next((odds for odds in data if odds['name'] == 'Rafał Trzaskowski'))['rate']['decimal']
    nawrocki_odds = next((odds for odds in data if odds['name'] == 'Karol Nawrocki'))['rate']['decimal']

    return {
        'bookmaker': 'LVBet',
        'trzaskowski': float(trzaskowski_odds),
        'nawrocki': float(nawrocki_odds)
    }