import requests
r = requests.get('https://get.geojs.io/')

ip_request = requests.get('https://get.geojs.io/v1/ip.json')
ipAdd = ip_request.json()['ip']

url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
geo_request = requests.get(url)
geo_data = geo_request.json()

print('Latitude coordinates', geo_data['latitude'])
print('Longitude coordinates', geo_data['longitude'])

print(geo_data['city'])
print(geo_data['region'])
print(geo_data['country'])
print(geo_data['timezone'])
