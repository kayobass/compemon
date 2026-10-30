from unittest.mock import MagicMock, patch

import pytest
import requests

from src.api.pokeapi import fetch_pokemon, list_pokemon_names


def test_list_pokemon_names_success():
    fake_response = MagicMock()
    fake_response.json.return_value = {
        "results": [
            {"name": "bulbasaur"},
            {"name": "ivysaur"},
            {"name": "venusaur"},
        ]
    }
    fake_response.raise_for_status = MagicMock()

    with patch("requests.get", return_value=fake_response) as mock_get:
        names = list_pokemon_names()
        assert names == ["bulbasaur", "ivysaur", "venusaur"]
        mock_get.assert_called_once()


def test_list_pokemon_names_timeout():
    with patch("requests.get", side_effect=requests.exceptions.Timeout):
        with pytest.raises(requests.exceptions.Timeout):
            list_pokemon_names()


def test_list_pokemon_names_http_error():
    with patch("requests.get", side_effect=requests.exceptions.HTTPError):
        with pytest.raises(requests.exceptions.HTTPError):
            list_pokemon_names()


def test_fetch_pokemon_success():
    pokemon_payload = {
        "name": "pikachu",
        "id": 25,
        "height": 4,
        "weight": 60,
        "base_experience": 112,
        "types": [{"type": {"name": "electric"}}],
        "stats": [
            {"stat": {"name": "hp"}, "base_stat": 35},
            {"stat": {"name": "attack"}, "base_stat": 55},
            {"stat": {"name": "defense"}, "base_stat": 40},
            {"stat": {"name": "special-attack"}, "base_stat": 50},
            {"stat": {"name": "special-defense"}, "base_stat": 50},
            {"stat": {"name": "speed"}, "base_stat": 90},
        ],
        "sprites": {
            "front_default": "default_sprite.png",
            "other": {
                "official-artwork": {
                    "front_default": "official_artwork.png"
                }
            },
        },
        "species": {"url": "https://pokeapi.co/api/v2/pokemon-species/25/"},
    }

    species_payload = {
        "color": {"name": "yellow"}
    }

    def mock_get(url, **kwargs):
        mock_resp = MagicMock()
        mock_resp.raise_for_status = MagicMock()
        if "pokemon-species" in url:
            mock_resp.json.return_value = species_payload
        else:
            mock_resp.json.return_value = pokemon_payload
        return mock_resp

    with patch("requests.get", side_effect=mock_get):
        result = fetch_pokemon("pikachu")

        assert result["name"] == "Pikachu"
        assert result["id"] == 25
        assert result["types"] == ["Electric"]
        assert result["height"] == 0.4
        assert result["weight"] == 6.0
        assert result["colour"] == "#FFD166"
        assert result["image"] == "official_artwork.png"
        assert result["attributes"]["attack"] == 55
        assert result["attributes"]["defence"] == 40


def test_fetch_pokemon_sprite_fallback():
    pokemon_payload = {
        "name": "ditto",
        "id": 132,
        "height": 3,
        "weight": 40,
        "base_experience": 101,
        "types": [{"type": {"name": "normal"}}],
        "stats": [
            {"stat": {"name": "hp"}, "base_stat": 48},
            {"stat": {"name": "attack"}, "base_stat": 48},
            {"stat": {"name": "defense"}, "base_stat": 48},
            {"stat": {"name": "special-attack"}, "base_stat": 48},
            {"stat": {"name": "special-defense"}, "base_stat": 48},
            {"stat": {"name": "speed"}, "base_stat": 48},
        ],
        "sprites": {
            "front_default": "default_sprite.png",
            "other": {
                "official-artwork": {
                    "front_default": None
                }
            },
        },
        "species": {},
    }

    mock_resp = MagicMock()
    mock_resp.raise_for_status = MagicMock()
    mock_resp.json.return_value = pokemon_payload

    with patch("requests.get", return_value=mock_resp):
        result = fetch_pokemon("ditto")
        # When official artwork is None, fallback to default sprite
        assert result["image"] == "default_sprite.png"


def test_fetch_pokemon_timeout():
    with patch("requests.get", side_effect=requests.exceptions.Timeout):
        with pytest.raises(requests.exceptions.Timeout):
            fetch_pokemon("mew")
