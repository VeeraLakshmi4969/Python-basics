import requests


base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    # because https://pokeapi.co/api/v2//pokemon/pikachu REALLY EXISTS
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        print("Data retrieved successfully (or)")
        data = response.json()
        print(data)
    else :
        print ("Data not retrieved successfully")
pokemon_name = "pikachu"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
     # it returns true when it exists
     print(f"{pokemon_info["name"]}")
     print(f"{pokemon_info["id"]}")
     print(f"{pokemon_info["weight"]}")
     # we have used these because these are exist in that api