from src.data.colours import DEFAULT_COLOURS, define_colours


def test_define_colours_unique(sample_pikachu, sample_charizard):
    pokemons = [sample_pikachu, sample_charizard]
    colours = define_colours(pokemons)

    assert isinstance(colours, dict)
    assert len(colours) == 2
    assert colours[sample_pikachu["id"]] == sample_pikachu["colour"]
    assert colours[sample_charizard["id"]] == sample_charizard["colour"]


def test_define_colours_duplicate(sample_pikachu):
    # Two Pokémon with identical colours
    pokemon_clone = {
        **sample_pikachu,
        "id": 26,  # Raichu
    }
    pokemons = [sample_pikachu, pokemon_clone]
    colours = define_colours(pokemons)

    assert len(colours) == 2
    assert colours[sample_pikachu["id"]] == sample_pikachu["colour"]
    assert colours[pokemon_clone["id"]] != sample_pikachu["colour"]
    assert colours[pokemon_clone["id"]] in DEFAULT_COLOURS


def test_define_colours_empty():
    assert define_colours([]) == {}
