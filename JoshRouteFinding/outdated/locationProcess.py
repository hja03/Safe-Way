import json

# Read the JSON content from the text file
with open("JoshRouteFinding/location.txt", "r") as file:
    content = file.read()

# Parse the JSON content
data = json.loads(content)

# Extract the latitude and longitude values
lat = data["results"][0]["geometry"]["location"]["lat"]
lng = data["results"][0]["geometry"]["location"]["lng"]

# Print the latitude and longitude values
print("Latitude:", lat)
print("Longitude:", lng)

print([lng, lat])