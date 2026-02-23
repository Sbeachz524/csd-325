import requests
import json

# API URL
url = "https://pokeapi.co/api/v2/pokemon/pikachu"

# Test connection
response = requests.get(url)
print("Status Code:", response.status_code)

# Raw response
print("\nRaw Response:")
print(response.text)

# Formatted JSON
print("\nFormatted JSON:")
data = response.json()
print(json.dumps(data, indent=4))

# Custom formatted output
print("\nPikachu Information:")
print("Name:", data['name'])
print("Height:", data['height'])
print("Weight:", data['weight'])

print("\nAbilities:")
for ability in data['abilities']:
    print("-", ability['ability']['name'])
