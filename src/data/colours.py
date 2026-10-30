DEFAULT_COLOURS = ["#469399", "#EBC6A2", "#394d36"]


def define_colours(pokemons: list[dict]) -> dict[int, str]:
    """Assign unique colours to each Pokémon for chart visualisation."""
    used_colours = set()
    colours = {}

    for pokemon in pokemons:
        colour = pokemon["colour"]

        if colour in used_colours:
            colour = next((c for c in DEFAULT_COLOURS if c not in used_colours), None)

        if colour is not None:
            used_colours.add(colour)

        colours[pokemon["id"]] = colour

    return colours
