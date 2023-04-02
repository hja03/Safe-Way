import requests
import json
# # home = "64 Brook Road, BA2 3RR"
# # Set the URL and parameters
# url = "https://maps.googleapis.com/maps/api/geocode/json"
# params = {
#     "address": "Labyrinth, Bath",
#     "key": "AIzaSyBFlEFbOWpgQYtHwDoqqS5XPIAenXK-SUw"
# }

# # Send the request
# response = requests.get(url, params=params)

# # Print the response content
# content_str = response.content.decode("utf-8")

# with open("JoshRouteFinding/location.txt", "w") as f:
#     f.write(content_str)

def get_long_lat(Location):
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
    "address": Location,
    "key": "AIzaSyBFlEFbOWpgQYtHwDoqqS5XPIAenXK-SUw"
    }

    # Send the request
    response = requests.get(url, params=params)

    # Print the response content
    content_str = response.content.decode("utf-8")

    # Parse the JSON content
    data = json.loads(content_str)

    # Extract the latitude and longitude values
    lat = data["results"][0]["geometry"]["location"]["lat"]
    lng = data["results"][0]["geometry"]["location"]["lng"]

    # Print the latitude and longitude values

    # print([lng, lat])

    return [lat, lng]

if __name__ == "__main__":
    print(get_long_lat("Labyrinth, Bath"))