import requests
from pprint import pprint
pokemon_number = input("What is the Pokemon's ID? ")
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
response = requests.get(url)
print(response)
pokemon = response.json()

moves = pokemon['moves']
for move in moves:
    print(move['move']['name'])
#    url1 = 'https://pokeapi.co/api/v2/move/{}/'.format(move)
#    response1 = requests.get(url)
#    move_characteristics = response1.json()
 #   print(move_characteristics['name'])