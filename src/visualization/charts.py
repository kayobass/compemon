import matplotlib.pyplot as plt
import numpy as np

from src.config import ATTRIBUTES

BACKGROUND_COLOUR = "#4A172C"


def _create_figure(**kwargs):
    fig, ax = plt.subplots(facecolor=BACKGROUND_COLOUR, **kwargs)
    ax.set_facecolor(BACKGROUND_COLOUR)

    return fig, ax


# Plot attribute bar chart


def plot_attribute_chart(pokemons: list[dict], colours: dict[int, str]):
    """Generate a grouped bar chart comparing Pokémon attributes."""
    fig, ax = _create_figure(figsize=(10, 6))

    attributes = list(ATTRIBUTES.values())
    positions = np.arange(len(ATTRIBUTES))
    spacing = 0.9
    bar_width = spacing / len(pokemons)

    for index, pokemon in enumerate(pokemons):
        values = [pokemon["attributes"][key] for key in ATTRIBUTES.keys()]
        offset = index * bar_width - spacing / 2 + bar_width / 2
        bars = ax.bar(
            positions + offset,
            values,
            bar_width,
            label=pokemon["name"],
            color=colours[pokemon["id"]],
        )
        ax.bar_label(bars, fontsize=8, color="white", padding=2)

    ax.set_xticks(positions)
    ax.set_title("Atributos por pokémon", color="white")
    ax.set_xticklabels(attributes, color="white")
    ax.set_ylabel("Valor base", color="white")
    ax.tick_params(colors="white")
    ax.legend(facecolor=BACKGROUND_COLOUR, labelcolor="white")

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.tight_layout()

    return fig


# Plot attribute radar chart


def plot_radar_chart(pokemons: list[dict], colours: dict[int, str]):
    """Generate a polar radar chart comparing Pokémon attributes."""
    fig, ax = _create_figure(figsize=(6, 6), subplot_kw={"polar": True})

    attribute_count = len(ATTRIBUTES)
    angles = np.linspace(0, 2 * np.pi, attribute_count, endpoint=False)
    angles = np.append(angles, angles[0])

    for pokemon in pokemons:
        values = [pokemon["attributes"][key] for key in ATTRIBUTES]
        values.append(values[0])
        ax.plot(
            angles,
            values,
            color=colours[pokemon["id"]],
            linewidth=2,
            label=pokemon["name"],
        )
        ax.fill(angles, values, color=colours[pokemon["id"]], alpha=0.2)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(ATTRIBUTES.values(), color="white")
    ax.tick_params(axis="y", colors="gray", labelsize=7)
    ax.tick_params(axis="x", colors="white", pad=12, rotation=15)
    ax.grid(color="gray", alpha=0.3)
    ax.set_title("Radar de atributos", color="white", pad=20)
    ax.legend(
        loc="upper right",
        bbox_to_anchor=(1.3, 1.1),
        facecolor=BACKGROUND_COLOUR,
        labelcolor="white",
    )
    fig.tight_layout()

    return fig


# Plot total attributes chart


def plot_total_chart(pokemons: list[dict], colours: dict[int, str]):
    """Generate a horizontal bar chart comparing Pokémon total attributes."""
    fig, ax = _create_figure(figsize=(6, 2.5))

    names = [pokemon["name"] for pokemon in pokemons]
    totals = [sum(pokemon["attributes"].values()) for pokemon in pokemons]
    bar_colours = [colours[pokemon["id"]] for pokemon in pokemons]

    bars = ax.barh(names, totals, color=bar_colours)

    ax.bar_label(bars, color="white", padding=2)
    ax.set_title("Total de Atributos", color="white")
    ax.tick_params(colors="white")
    ax.set_xlim(0, max(totals) * 1.15)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.tight_layout()

    return fig
