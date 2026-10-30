import pytest


@pytest.fixture
def sample_pikachu():
    return {
        "name": "Pikachu",
        "id": 25,
        "types": ["Electric"],
        "attributes": {
            "hp": 35,
            "attack": 55,
            "defence": 40,
            "special_attack": 50,
            "special_defence": 50,
            "speed": 90,
            "base_exp": 112,
        },
        "height": 0.4,
        "weight": 6.0,
        "colour": "#FFD166",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png",
    }


@pytest.fixture
def sample_charizard():
    return {
        "name": "Charizard",
        "id": 6,
        "types": ["Fire", "Flying"],
        "attributes": {
            "hp": 78,
            "attack": 84,
            "defence": 78,
            "special_attack": 109,
            "special_defence": 85,
            "speed": 100,
            "base_exp": 267,
        },
        "height": 1.7,
        "weight": 90.5,
        "colour": "#FF5959",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png",
    }


@pytest.fixture
def sample_bulbasaur():
    return {
        "name": "Bulbasaur",
        "id": 1,
        "types": ["Grass", "Poison"],
        "attributes": {
            "hp": 45,
            "attack": 49,
            "defence": 49,
            "special_attack": 65,
            "special_defence": 65,
            "speed": 45,
            "base_exp": 64,
        },
        "height": 0.7,
        "weight": 6.9,
        "colour": "#6BCB77",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/1.png",
    }


@pytest.fixture
def sample_pokemons(sample_pikachu, sample_charizard):
    return [sample_pikachu, sample_charizard]
