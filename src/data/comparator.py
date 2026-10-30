from itertools import combinations

import numpy as np
import pandas as pd

from src.config import ATTRIBUTES


def _format_difference(difference: float, percentage: float) -> str:
    """Format the numerical and percentage difference between two values."""
    if pd.isna(difference):
        return "-"

    if pd.isna(percentage):
        return f"{difference:+.0f} (N/A)"

    if difference > 0:
        return f"▲ {difference:+.1f} ({percentage:+.1f}%)"

    if difference < 0:
        return f"▼ {difference:.1f} ({percentage:.1f}%)"

    return f"= {difference:.1f} ({percentage:.1f}%)"


def colour_difference(value: object) -> str:
    """Return CSS styling to colour difference values in DataFrame cells."""
    text_value = str(value)

    if "▲" in text_value:
        return "color: #4CAF50; font-weight: bold"

    if "▼" in text_value:
        return "color: #FC7B03; font-weight: bold"

    return "color: #D9A441; font-weight: bold"


def build_comparison_table(pokemons: list[dict]) -> pd.DataFrame:
    """Build a comparison table DataFrame for the selected Pokémon."""
    rows = {}

    for key, label in ATTRIBUTES.items():
        rows[label] = [pokemon["attributes"][key] for pokemon in pokemons]

    rows["Total"] = [sum(pokemon["attributes"].values()) for pokemon in pokemons]

    names = [pokemon["name"] for pokemon in pokemons]
    table = pd.DataFrame(rows, index=names).T

    for first_name, second_name in combinations(names, 2):
        column_name = f"{second_name} vs {first_name}"
        difference = table[second_name] - table[first_name]
        percentage = (
            difference / table[first_name].replace(0, np.nan)
        ) * 100

        table[column_name] = [
            _format_difference(diff, pct)
            for diff, pct in zip(difference, percentage)
        ]

    return table
