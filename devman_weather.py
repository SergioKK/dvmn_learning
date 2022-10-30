import requests

locations = ['London', 'Cherepovets', 'Sheremetyevo airport']
payload = {'nTqM': '', 'lang': 'ru'}

for location in locations:
    try:
        response = requests.get('http://wttr.dvmn.org/'+location, params=payload)
        response.raise_for_status()
        print(response.text)
    except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError):
        print('Something went wrong, please try again later')
    
