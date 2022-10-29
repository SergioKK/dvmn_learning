import requests

urls = ['http://wttr.dvmn.org/London', 'http://wttr.dvmn.org/Cherepovets', 'http://wttr.dvmn.org/Sheremetyevo+airport']
payload = {'lang': 'ru', 'nTqu': ''}

for url in urls:
    try:
        response = requests.get(url, params=payload)
        response.raise_for_status()
        print(response.text)
    except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError):
        print('Something went wrong, please try again later')
