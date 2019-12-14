import requests
from apikeys import hueuser
from colorConverter import RGBtoXY

# r = requests.post('http://192.168.7.28/api/',
#                   json={'devicetype': 'hue-airly-app'})

# print(r.status_code)
# print(r.json())
# r = requests.get('http://192.168.7.28/api/'+hueuser+'/lights/14')
xh = RGBtoXY(211, 34, 11)
r = requests.put(
    'http://192.168.7.28/api/'+hueuser+'/lights/14/state', json={'on': True, 'bri': 10, 'xy': xh})
# print(colorsys.rgb_to_hls(100, 134, 122))
# print(r.status_code)
# print(r.json())
