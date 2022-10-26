import requests

url_London = 'http://wttr.dvmn.org/London?nTqu&lang=en'
url_Cherepovets = 'http://wttr.dvmn.org/Cherepovets?nTMq&lang=ru'
url_Sheremetyevo_airport = 'http://wttr.dvmn.org/Sheremetyevo+airport?nTMq&lang=ru'

response_London = requests.get(url_London)
response_Cherepovets = requests.get(url_Cherepovets)
response_Sheremetyevo_airport = requests.get(url_Sheremetyevo_airport)

print(response_London.text)
print(response_Cherepovets.text)
print(response_Sheremetyevo_airport.text)
