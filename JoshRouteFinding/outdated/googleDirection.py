import requests

# Replace YOUR_API_KEY with your actual API key
api_key = 'AIzaSyBFlEFbOWpgQYtHwDoqqS5XPIAenXK-SUw'

# Set the origin and destination addresses
origin = 'Labrynth Bath'
destination = '64 Brook Road, BA23RR'

# Set the API endpoint URL
url = f'https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={api_key}'

# Send the API request and get the response
response = requests.get(url)

content_str = response.content.decode("utf-8")

with open("JoshRouteFinding/googleDirections.txt", "w") as f:
    f.write(content_str)

# Print the status code and response content
# print(response.status_code, response.reason)
# print(content_str)
