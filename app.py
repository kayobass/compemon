import requests
import streamlit as st

from src.api.pokeapi import (
    fetch_pokemon,
    list_pokemon_names,
)
from src.data.colours import define_colours
from src.data.comparator import (
    build_comparison_table,
    colour_difference,
)
from src.visualization.charts import (
    plot_attribute_chart,
    plot_radar_chart,
    plot_total_chart,
)

st.set_page_config(
    page_title="Compémon",
    page_icon="⚡",
    layout="wide",
)

st.title("⚡ Compémon")
st.caption("## Compare os atributos dos seus Pokémons favoritos!")

st.subheader("Escolha seus Pokémons")

try:
    pokemon_names = st.cache_data(list_pokemon_names)()
except requests.exceptions.Timeout:
    st.error("⏳ A PokéAPI demorou demais para responder. Tente novamente.")
except requests.exceptions.HTTPError as http_error:
    status_code = http_error.response.status_code
    st.error(f"🌐 A PokéAPI retornou um erro HTTP ({status_code}).")
except requests.exceptions.RequestException:
    st.error("🔌 Ocorreu um problema na comunicação com a PokéAPI. Verifique sua conexão e tente novamente.")

cached_fetch_pokemon = st.cache_data(fetch_pokemon)

selected_pokemons = st.multiselect(
    "Escolha de 2 a 3 Pokémon (digite para buscar):",
    options=pokemon_names,
    max_selections=3,
    format_func=lambda name: name.replace("-", " ").title(),
)

if len(selected_pokemons) < 2:
    st.info("Selecione pelo menos 2 Pokémon para comparar.")
    st.stop()

try:
    with st.spinner("Buscando dados dos Pokémons..."):
        pokemons = [cached_fetch_pokemon(name) for name in selected_pokemons]
        colours = define_colours(pokemons)
except requests.exceptions.Timeout:
    st.error("⏳ A PokéAPI demorou demais para responder. Tente novamente.")
except requests.exceptions.HTTPError as http_error:
    status_code = http_error.response.status_code
    st.error(f"🌐 A PokéAPI retornou um erro HTTP ({status_code}).")
except requests.exceptions.RequestException:
    st.error("🔌 Ocorreu um problema na comunicação com a PokéAPI. Verifique sua conexão e tente novamente.")

st.subheader("Atributos dos Pokémons Selecionados:")

columns = st.columns(len(selected_pokemons))

for column, pokemon in zip(columns, pokemons):
    with column:
        if pokemon["image"]:
            st.image(pokemon["image"], width=250)

        st.subheader(f"{pokemon['name']} #{pokemon['id']}")

        st.write(f"""
            Altura: {pokemon['height']:g}m
            | Peso: {pokemon['weight']:g}KG

            Tipo: {' / '.join(pokemon['types'])}
        """)

st.divider()
st.subheader("📊 Tabela de comparação")
st.caption("Em cada coluna 'X vs Y', a porcentagem mostra quanto X está acima (▲) ou abaixo (▼) de Y.")

table = build_comparison_table(pokemons)

difference_columns = [
    column for column in table.columns
    if " vs " in column
]

styled_table = table.style.map(
    colour_difference,
    subset=difference_columns,
).format(
    "{:.1f}",
    subset=table.columns.drop(difference_columns),
)

st.dataframe(styled_table, width="stretch")

st.divider()
st.subheader("📈 Gráficos")

left_column, right_column = st.columns([3, 2])

with left_column:
    st.pyplot(plot_attribute_chart(pokemons, colours))

with right_column:
    st.pyplot(plot_radar_chart(pokemons, colours))

st.divider()

total_column, _ = st.columns([3, 2])
with total_column:
    st.pyplot(plot_total_chart(pokemons, colours))
