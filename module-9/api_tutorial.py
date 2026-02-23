import requests
import json

# Test connection
response = requests.get('http://api.open-notify.org/astros.json')
print("Status Code:", response.status_code)

# Raw JSON response
print("\nRaw JSON Response:")
print(response.text)

# Formatted JSON output
print("\nFormatted Output:")
data = response.json()
print(json.dumps(data, indent=4))

# Print astronaut names
print("\nAstronauts Currently in Space:")
for person in data['people']:
    print("-", person['name'])
import requests

response = requests.get('http://api.open-notify.org/astros.json')
print(response.status_code)

