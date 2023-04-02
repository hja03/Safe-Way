import json

with open('JoshRouteFinding\googleDirections.txt') as f:
    data = json.load(f)

for route in data['routes']:
    for leg in route['legs']:
        start_lat = leg['start_location']['lat']
        start_lng = leg['start_location']['lng']
        end_lat = leg['end_location']['lat']
        end_lng = leg['end_location']['lng']
        print(f'Start: ({start_lat}, {start_lng})')
        print(f'End: ({end_lat}, {end_lng})')

