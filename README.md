<p align="center">
  <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" height="60" width="60">
</p>

<div align="center">
  <h1>PokéAPI</h1>
</div>

This Python script enables users to retrieve detailed information about a Pokémon by its name using PokeAPI. After entering a Pokémon's name, the script sends a GET request to the API and presents details such as the Pokémon's name, abilities, types, and ID.

## Resources:
My script was developed with guidance from [Bro Code](https://www.youtube.com/watch?v=JVQNywo4AbU), whose tutorial helped in understanding how to interact with APIs in Python.

## Code Walkthrough:
#### Library:
```python
  import requests
```

  - ` requests `: Used for sending HTTP requests.

#### Base URL:
```python
  base_url = "https://pokeapi.co/api/v2/"
```

  - Sets the base URL for the Pokémon API. Setting a base URL is a fundamental aspect when working with APIs.
  - **Important:**
    - The base URL is the starting point for all endpoints provided by an API. It defines the primary address used to request specific resources.

#### get_pokemon_info Function and Response Handling:
```python
  def get_pokemon_info(name):
    url = f"{base_url}pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to get data. Status code: {response.status_code}")
        return
```

  - **Purpose:** Fetches information about a Pokémon from PokéAPI.
  - **How it works:**
    - ` url = f"{base_url}pokemon/{name}" `: Constructs the full URL for the API request by appending the Pokémon name to the base URL.
    - ` response = requests.get(url) `: Sends an HTTP GET request to the constructed URL to fetch the Pokémon information.
    - ` if response.status_code == 200: `: Checks if the status code of the response is 200, which indicates a successful request.
    - ` pokemon_data = response.json() `: If the request is successful, the response is converted from JSON format to a Python dictionary and stored in ` pokemon_data `.
    - `return pokemon_data `: The function returns the ` pokemon_data ` dictionary, which contains the Pokémon information.
    - ` else: `: If the status code is not 200, the function prints an error message with the status code.

#### Fetching Pokémon Info:
```python
  pokemon_info = get_pokemon_info(pokemon_name)
```

  - Fetches the Pokémon information using the ` get_pokemon_info ` function with the user-provided name.

#### Output:
```python
  if pokemon_info:
    print(f"Name: {pokemon_info['name'].capitalize()}")
    print(f"{abilities_label}: {abilities}")
    print(f"{types_label}: {types}")
    print(f"ID: {pokemon_info['id']}")
```

  - If the Pokémon info is successfully retrieved, prints the name, ability, type and ID.

## Development Environment:
This project was developed using the following tools and versions:
  - Visual Studio Code: 1.96.4
  - Python: 3.13.1

## Contact:
Feel free to reach out to me with any questions, suggestions, or feedback!<br/>
[![GitHub](https://github.com/CLorant/readme-social-icons/blob/main/large/filled/github.svg)](https://github.com/mateuszcalderon)
[![Instagram](https://github.com/CLorant/readme-social-icons/blob/main/large/filled/instagram.svg)](https://www.instagram.com/mateuszcalderon/)
[![LinkedIn](https://github.com/CLorant/readme-social-icons/blob/main/large/filled/linkedin.svg)](https://www.linkedin.com/in/mateuszcalderonreis/)
