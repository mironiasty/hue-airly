import requests
from apikeys import hueuser
from colorConverter import RGBtoXY
from airly import GetAirColor

color = GetAirColor()
xyColor = RGBtoXY(color['red'], color['green'], color['blue'])
r = requests.put(
    'http://192.168.7.28/api/'+hueuser+'/lights/14/state',
    json={'on': True, 'bri': 70, 'xy': xyColor})
