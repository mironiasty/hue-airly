import requests

r = requests.post('http://192.168.7.28/api/',
                  json={'devicetype': 'hue-airly-app'})

print(r.status_code)
print(r.json())

# get lamps info
# r = requests.get('http://192.168.7.28/api/'+hueuser+'/lights')
