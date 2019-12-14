import requests
from apikeys import airlykey, location


def ConvertColor(color):
    return {'red': int(color[1:3], 16), 'green': int(color[3:5], 16), 'blue': int(color[5:7], 16)}


def GetAirColor():
    request = requests.get('https://airapi.airly.eu/v2/measurements/point?lat=' + str(location['latitude']) + '&lng=' + str(location['longitude']), headers={
        'Accept': 'application/json', 'apikey': airlykey, 'Accept-Language': 'pl'
    })
    color = request.json()['current']['indexes'][0]['color']
    # color = "#6BC926"
    return ConvertColor(color)


# print(GetAirColor())
