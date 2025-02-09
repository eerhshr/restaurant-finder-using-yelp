import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()
DEFAULT_TERM = ''
API_KEY = os.getenv('API_KEY')
API_HOST = os.getenv('API_HOST')
SEARCH_PATH = os.getenv('SEARCH_PATH')
BUSINESS_PATH = os.getenv('BUSINESS_PATH')


def get_data(location, term=DEFAULT_TERM, radius=1600):
    try:
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
    except:
        print('Error getting data')