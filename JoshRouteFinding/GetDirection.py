import requests
import copy
import json

def get_directions(start, end, driving=False, cycling=False):
    # Flipping Longitude and latitude
    start = copy.deepcopy(start)
    start.reverse()
    end = copy.deepcopy(end)
    end.reverse()

    body = {f"coordinates": [start,end]}

    headers = {
    'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
    'Authorization': '5b3ce3597851110001cf624813d933ec206b49f98c8c67932b311c50',
    'Content-Type': 'application/json; charset=utf-8'
    }
    direction_type = "foot-walking"
    if driving:
        direction_type = "driving-car"

    elif cycling:
        direction_type = "cycling-regular"

    call = requests.post(f'https://api.openrouteservice.org/v2/directions/{direction_type}/geojson', json=body, headers=headers)
    # print(call.text)
    api_response = json.loads(call.text)
    
    # Extract the geometry values
    try:
        route = api_response['features'][0]['geometry']['coordinates']
    except:
        print("error")
        print(api_response)

    # Reversing Longitude and Latitudes
    newRoute = []
    for r in route:
        r.reverse()
        newRoute.append(r)

    return newRoute

if __name__ == "__main__":
    print(get_directions([51.380679, -2.3567243],[51.3804147, -2.3815838]))