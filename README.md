<p align="center">
  <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" height="60" width="60">
</p>

<div align="center">
  <h1>PokéAPI</h1>
</div>

## Code Walkthrough:
#### Library:
```python
  import requests
```

  - ` requests `: Used for sending HTTP requests

#### Base URL:
```python
  base_url = 'https://pokeapi.co/api/v2/'
```

  - Sets the base URL for the Pokémon API. Setting a base URL is a fundamental aspect when working with APIs
  - The base URL is the starting point for all endpoints provided by the API. It defines the primary address used to request specific resources

#### get_pokemon_info Function and Response Handling:
```python
  def get_pokemon_info(name):
    url = f'{base_url}pokemon/{name}'
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f'Failed to get Data {response.status_code}')
        return
```

  - **Purpose:** Fetches information about a Pokémon from the PokéAPI
  - **How it works:**
    - ` url = f'{base_url}pokemon/{name}' `: Constructs the full URL for the API request by appending the Pokémon name to the base URL
    - ` response = requests.get(url) `: Sends an HTTP GET request to the constructed URL to fetch the Pokémon information
    - ` if response.status_code == 200: `: Checks if the status code of the response is 200, which indicates a successful request
    - ` pokemon_data = response.json() `: If the request is successful, the response is converted from JSON format to a Python dictionary and stored in the ` pokemon_data ` variable
    - `return pokemon_data `: The function returns the ` pokemon_data ` dictionary, which contains the Pokémon information
    - ` else: `: If the status code is not 200, the function prints an error message with the status code

#### Fetching Pokémon Info:
```python
  pokemon_info = get_pokemon_info(pokemon_name)
```

  - Fetches the Pokémon information using the ` get_pokemon_info ` function with the user-provided name

#### Output:
```python
  if pokemon_info:
    print(f'Name: {pokemon_info["name"].capitalize()}')
    print(f'ID: {pokemon_info["id"]}')
    print(f'Height: {pokemon_info["height"]}')
    print(f'Weight: {pokemon_info["weight"]}')
```

  - If the Pokémon info is successfully retrieved, prints the name, ID, height, and weight

## Development Environment:
This project was developed using the following tools and versions:
  - Visual Studio Code: 1.96.4
  - Python: 3.13.1
