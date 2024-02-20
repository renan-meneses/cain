import requests


def get_data_from_endpoint(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            dados = response.json()
            return dados
        else:
            print(f"Status: {response.status_code}")  # noaq: E501
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error when making the request: {e}")
        return None
