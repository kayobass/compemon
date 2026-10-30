# ⚡ Compémon

Uma aplicação web interativa em **Streamlit** para comparar atributos e estatísticas dos seus Pokémons favoritos consumindo dados em tempo real da [PokéAPI](https://pokeapi.co/).

---

## 🎯 Funcionalidades

- **Seleção Dinâmica:** Busque e selecione de 2 a 3 Pokémon para comparação lado a lado.
- **Fichas Informativas:** Visualize imagem oficial, número da Pokédex, tipos, altura e peso de cada Pokémon.
- **Tabela Comparativa:**
  - Confronto direto de atributos (`HP`, `Ataque`, `Defesa`, `Ataque Especial`, `Defesa Especial`, `Velocidade` e `Total`).
  - Cálculo automático de diferença numérica e percentual (`X vs Y`), com destaque visual colorido para vantagens (▲ verde) e desvantagens (▼ laranja).
- **Gráficos Comparativos (Matplotlib):**
  - **Gráfico de Barras Agrupadas:** Comparação de cada atributo base individualmente.
  - **Gráfico de Radar:** Visão geral equilibrada dos atributos no plano polar.
  - **Gráfico de Totais:** Barra horizontal com a soma total das estatísticas base.

---

## 🛠️ Tecnologias

- **Linguagem:** [Python](https://www.python.org/)
- **Interface Web:** [Streamlit](https://streamlit.io/)
- **Consumo de API:** [Requests](https://requests.readthedocs.io/)
- **Processamento de Dados:** [Pandas](https://pandas.pydata.org/) e [NumPy](https://numpy.org/)
- **Visualização de Dados:** [Matplotlib](https://matplotlib.org/)
- **Testes Automatizados:** [Pytest](https://docs.pytest.org/)
- **Gerenciador de Dependências:** [uv](https://docs.astral.sh/uv/)

---

## 📂 Estrutura do Projeto

```text
Compemon/
├── app.py                     # Ponto de entrada da aplicação Streamlit
├── src/
│   ├── api/
│   │   └── pokeapi.py         # Integração e normalização de dados da PokéAPI
│   ├── config.py              # Dicionário de atributos e configurações
│   ├── data/
│   │   ├── colours.py         # Lógica de atribuição e unicidade de cores
│   │   └── comparator.py      # Construção da tabela e cálculos de diferença
│   └── visualization/
│       └── charts.py          # Gráficos de barras, radar e total
├── tests/                     # Suíte de testes unitários com pytest
│   ├── conftest.py            # Fixtures de Pokémon para testes
│   ├── test_charts.py         # Testes dos gráficos
│   ├── test_colours.py        # Testes do gerador de cores
│   ├── test_comparator.py     # Testes da tabela e formatação de diferenças
│   └── test_pokeapi.py        # Testes com mocks da PokéAPI
├── pyproject.toml             # Metadados e dependências do projeto
├── requirements.txt           # Dependências pip
└── README.md
```

---

## 🚀 Como Executar

### 1. Pré-requisitos
Certifique-se de ter o Python instalado ou o [uv](https://docs.astral.sh/uv/).

### 2. Instalar as dependências

Com **uv** (recomendado):
```bash
uv sync
```

Ou com **pip**:
```bash
pip install -r requirements.txt
```

### 3. Iniciar a aplicação

Com **uv**:
```bash
uv run streamlit run app.py
```

Ou diretamente:
```bash
streamlit run app.py
```

A aplicação será aberta automaticamente no seu navegador padrão (geralmente em `http://localhost:8501`).

---

## 🧪 Como Rodar os Testes

Para executar os testes automatizados com o `pytest`:

```bash
uv run pytest -v
```
