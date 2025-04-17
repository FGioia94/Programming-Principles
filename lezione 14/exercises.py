import requests 
import json
response = requests.get("https://pokeapi.co/api/v2/pokemon/octillery") 
try:
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    print("Errore nella richiesta")
else:
    if response.status_code == 200:
        print("Richiesta Riuscita")
        data = response.json()
        with open("ditto.json", "w", encoding = "utf-8") as file:
            json.dump(data, file, indent = 4)
        print(data)
        height = data["height"]
        pokemon_sprite_url = data["sprites"]["front_default"]
        pokemon_cry_url = data["cries"]["latest"]
        with open("sprite.png", "wb") as file:
            sprite_response = requests.get(pokemon_sprite_url)
            file.write(sprite_response.content)
        with open("cry.ogg", "wb") as file:
            cry_response = requests.get(pokemon_cry_url)
            file.write(cry_response.content)