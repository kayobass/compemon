import numpy as np
import pandas as pd

from src.config import ATTRIBUTES
from src.data.comparator import (
    _format_difference,
    build_comparison_table,
    colour_difference,
)


def test_format_difference_positive():
    formatted = _format_difference(10.0, 25.5)
    assert formatted == "▲ +10.0 (+25.5%)"


def test_format_difference_negative():
    formatted = _format_difference(-5.0, -12.5)
    assert formatted == "▼ -5.0 (-12.5%)"


def test_format_difference_zero():
    formatted = _format_difference(0.0, 0.0)
    assert formatted == "= 0.0 (+0.0%)" or formatted == "= 0.0 (0.0%)"


def test_format_difference_nan_difference():
    assert _format_difference(np.nan, 10.0) == "-"


def test_format_difference_nan_percentage():
    assert _format_difference(15.0, np.nan) == "+15 (N/A)"


def test_colour_difference_styles():
    assert "color: #4CAF50" in colour_difference("▲ +10.0 (+20%)")
    assert "color: #FC7B03" in colour_difference("▼ -5.0 (-10%)")
    assert "color: #D9A441" in colour_difference("= 0.0 (0%)")
    assert "color: #D9A441" in colour_difference("-")


def test_build_comparison_table_structure(sample_pokemons):
    table = build_comparison_table(sample_pokemons)

    assert isinstance(table, pd.DataFrame)
    # Pokémon columns and comparison column
    assert "Pikachu" in table.columns
    assert "Charizard" in table.columns
    assert "Charizard vs Pikachu" in table.columns

    # Check index contains all attributes and Total
    for label in ATTRIBUTES.values():
        assert label in table.index
    assert "Total" in table.index


def test_build_comparison_table_totals(sample_pikachu, sample_charizard):
    table = build_comparison_table([sample_pikachu, sample_charizard])

    expected_pikachu_total = sum(sample_pikachu["attributes"].values())
    expected_charizard_total = sum(sample_charizard["attributes"].values())

    assert table.loc["Total", "Pikachu"] == expected_pikachu_total
    assert table.loc["Total", "Charizard"] == expected_charizard_total
