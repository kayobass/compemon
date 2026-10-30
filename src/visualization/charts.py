import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go

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
    """Generate an interactive radar chart comparing Pokémon attributes."""
    fig = go.Figure()

    labels = list(ATTRIBUTES.values())

    for pokemon in pokemons:
        values = [
            pokemon["attributes"][key]
            for key in ATTRIBUTES
        ]

        closed_values = values + [values[0]]
        categories = labels + [labels[0]]

        colour = colours[pokemon["id"]]

        r = int(colour[1:3], 16)
        g = int(colour[3:5], 16)
        b = int(colour[5:7], 16)

        fig.add_trace(
            go.Scatterpolar(
                r=closed_values,
                theta=categories,
                fill="toself",
                fillcolor=f"rgba({r}, {g}, {b}, 0.2)",
                line=dict(
                    color=colour,
                    width=2
                ),
                name=pokemon["name"],
            )
        )

    fig.update_layout(
        title="Radar de atributos",
        polar=dict(
            bgcolor=BACKGROUND_COLOUR,
            radialaxis=dict(
                visible=True,
                gridcolor="rgba(255,255,255,0.2)",
                tickfont=dict(color="gray", size=12),
            ),
            angularaxis=dict(
                gridcolor="rgba(255,255,255,0.2)",
                tickfont=dict(color="white", size=13),
            ),
        ),
        paper_bgcolor=BACKGROUND_COLOUR,
        font=dict(color="white"),
        legend=dict(
            bgcolor=BACKGROUND_COLOUR,
            font=dict(color="white"),
        ),
        height=700,
        margin=dict(l=65, r=65, t=75, b=55),
    )

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
