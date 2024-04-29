import json
import requests
import os
from dotenv import load_dotenv

API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'

load_dotenv()
DEFAULT_TERM = 'dinner'
API_KEY = os.getenv('API_KEY')


def get_data(location, term=DEFAULT_TERM, radius=1600):
    base_url = API_HOST + SEARCH_PATH
    headers = {
        'Authorization': f'Bearer {API_KEY}',
    }
    params = {
        'term': term,
        'location': location,
        'radius': radius,
    }

    response = requests.get(base_url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        with open("sampleData.json", "w") as outfile:
            json.dump(data, outfile, indent=2)
    else:
        print(f'{response.status_code} : Failed to retrieve data.')
