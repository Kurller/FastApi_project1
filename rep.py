import requests


api_url = 'https://nubela.co/proxycurl/api/v2/linkedin/company/job'
api_key = 'DlmmJ1o8l6fUf8AvtQ9Bvw'

def fetch_data_from_api(api_url, api_key):
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data from the API. Status code: {response.status_code}")
        return None
fetch_data_from_api(api_url, api_key)