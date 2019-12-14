import requests
from apikeys import hueuser

r = requests.put(
    'http://192.168.7.28/api/'+hueuser+'/lights/14/state',
    json={'on': False})
