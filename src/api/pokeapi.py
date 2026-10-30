import requests

BASE_URL = "https://pokeapi.co/api/v2"

COLOUR_BY_NAME = {
    "red": "#FF5959",
    "blue": "#4DB6FF",
    "yellow": "#FFD166",
    "green": "#6BCB77",
    "black": "#404040",
    "brown": "#694c3e",
    "purple": "#B388EB",
    "gray": "#75726b",
    "grey": "#75726b",
    "white": "#F5F5F5",
    "pink": "#FF9ECD",
    "lime": "#B5F556",
}


def list_pokemon_names() -> list[str]:
    """Fetch the list of all Pokémon names available from the PokéAPI."""
    url = f"{BASE_URL}/pokemon?limit=2000&offset=0"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()["results"]

        return [pokemon["name"] for pokemon in data]

    except requests.exceptions.Timeout:
        print("Request timed out.")
        raise

    except requests.exceptions.HTTPError:
        print("The API returned an HTTP error.")
        raise

    except requests.exceptions.RequestException as error:
        print(f"Request error: {error}")
        raise


def fetch_pokemon(name: str) -> dict:
    """Fetch detailed data for a specific Pokémon by its name."""
    url = f"{BASE_URL}/pokemon/{name.strip().lower()}"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        stats = {
            stat["stat"]["name"]: stat["base_stat"]
            for stat in data["stats"]
        }

        colour_name = "lime"
        if data["species"].get("url"):
            species_response = requests.get(data["species"]["url"], timeout=10)
            species_response.raise_for_status()
            species_data = species_response.json()

            colour_name = species_data.get("color", {}).get("name", "lime")

        image_url = data["sprites"]["other"]["official-artwork"]["front_default"]
        if image_url is None:
            image_url = data["sprites"]["front_default"]

        return {
            "name": data["name"].replace("-", " ").title(),
            "id": data["id"],
            "types": [
                pokemon_type["type"]["name"].title()
                for pokemon_type in data["types"]
            ],
            "attributes": {
                "hp": stats["hp"],
                "attack": stats["attack"],
                "defence": stats["defense"],
                "special_attack": stats["special-attack"],
                "special_defence": stats["special-defense"],
                "speed": stats["speed"],
                "base_exp": data["base_experience"],
            },
            "height": data["height"] / 10,
            "weight": data["weight"] / 10,
            "colour": COLOUR_BY_NAME.get(colour_name, "#B5F556"),
            "image": image_url,
        }

    except requests.exceptions.Timeout:
        print("Request timed out.")
        raise

    except requests.exceptions.HTTPError:
        print("The API returned an HTTP error.")
        raise

    except requests.exceptions.RequestException as error:
        print(f"Request error: {error}")
        raise
