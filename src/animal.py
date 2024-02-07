import os
import requests

def getCats():
    print('Finding animals that match "cat"...')

    headers = {
        'X-Api-Key': os.environ.get('API_KEY')
    }
    params = {
        'name': 'cat'
    }
    animalApiResponse = requests.get('https://api.api-ninjas.com/v1/animals', headers=headers, params=params)
    animals = animalApiResponse.json()

    if len(animals) == 0:
        print('No matches found')
        return

    print(f'Found {len(animals)} matches:')
    for animal in animals:
        print(animal['name'])