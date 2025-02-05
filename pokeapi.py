import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}pokemon/{name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to get data. Status code: {response.status_code}")
        return

pokemon_name = input("Enter a Pokémon Name: ").lower()
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    abilities = ", " .join([ability['ability']['name'] for ability in pokemon_info['abilities']])
    abilities_label = "Abilities" if len(pokemon_info['abilities']) > 1 else "Ability"
    types = ", ".join([type['type']['name'] for type in pokemon_info['types']])
    types_label = "Types" if len(pokemon_info['types']) > 1 else "Type"
    print(f"Name: {pokemon_info['name'].capitalize()}")
    print(f"{abilities_label}: {abilities}")
    print(f"{types_label}: {types}")
    print(f"ID: {pokemon_info['id']}")
