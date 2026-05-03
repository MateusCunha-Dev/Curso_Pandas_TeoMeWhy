# %%
import pandas as pd
from IPython.display import display

PATH = "../../data/transacoes.csv"
df_transacoes = pd.read_csv(PATH, sep=";")

# %%
df_transacoes.shape

# %%
df_transacoes.info(memory_usage='deep')

# %%
df_transacoes.dtypes

# %%
print("\nRenomeando colunas específicas")
renamed_columns = {"QtdePontos": "qtPontos",
                   "DescSistemaOrigem": "sistemaOrigem"}

df_transacoes = df_transacoes.rename(columns=renamed_columns)
"""df_transacoes.rename(columns=renamed_columns, inplace=True)""" # Forma de renomear sem precisar reatribuir o DataFrame

# %%
df_transacoes

# %%
print("\nForma de buscar mais de uma coluna do DataFrame")
df_transacoes[["IdCliente","qtPontos"]].head(5)
# %%

print("\nOrdenando as colunas do DataFrame (ordem alfabética)")
colunas = df_transacoes.columns.sort_values().to_list()
df_transacoes = df_transacoes[colunas]

# %%
display(df_transacoes)
# %%
