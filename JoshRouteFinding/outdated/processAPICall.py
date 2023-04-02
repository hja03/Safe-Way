import json

# Read the API response from the txt file
with open('JoshRouteFinding/my_file.txt', 'r') as f:
    api_response = json.load(f)

# Extract the geometry values
geometry_coords = api_response['features'][0]['geometry']['coordinates']

# Print the geometry coordinates
print(geometry_coords)

