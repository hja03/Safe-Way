import requests
# longitude, latiude
body = {"coordinates":[[-2.3815838,51.3804147],[-2.3567243,51.380679]]}

headers = {
    'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
    'Authorization': '5b3ce3597851110001cf624813d933ec206b49f98c8c67932b311c50',
    'Content-Type': 'application/json; charset=utf-8'
}
call = requests.post('https://api.openrouteservice.org/v2/directions/foot-walking/geojson', json=body, headers=headers)

print(call.status_code, call.reason)
print(call.text)


with open("JoshRouteFinding/my_file.txt", "w") as f:
    f.write(call.text)

