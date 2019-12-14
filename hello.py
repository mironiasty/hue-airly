import requests
import math
from apikeys import hueuser


# r = requests.post('http://192.168.7.28/api/',
#                   json={'devicetype': 'hue-airly-app'})

# print(r.status_code)
# print(r.json())
r = requests.get('http://192.168.7.28/api/'+hueuser+'/lights/')
print(r.status_code)
print(r.json())
