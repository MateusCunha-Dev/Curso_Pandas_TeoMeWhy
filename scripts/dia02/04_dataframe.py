# %%
import pandas as pd
from IPython.display import display

PATH = "../../data/clientes.csv"
df_clientes = pd.read_csv(PATH, sep=";")


# %%
print("\nMétodo .head() para visualizar os 10 primeiros registros")
display(df_clientes.head(10))

# %%
print("\nMétodo .tail() para visualizar os 10 últimos registros")
display(df_clientes.tail(10))

# %%
print("\nMétodo .sample() para visualizar 10 registros aleatórios")
display(df_clientes.sample(10))

# %%
print("\nAtributo .shape para visualizar a quantidade de linhas e colunas de um DataFrame")
df_clientes.shape

# %%
print("\nAtributo .columms que mostra todas as colunas")
df_clientes.columns

# %%
print("\nAtributo .index que mostra os índices")
df_clientes.index

# %%
print("\nMétodo .info() fornece um resumo técnico completo do DataFrame")
df_clientes.info()

# %%
print("\nRetorna uma lista (Series) com os nomes de todas as colunas e seus respectivos tipos de dados ao lado")
df_clientes.dtypes

# %%
print("\nNesse caso, vai na coluna especificada e retorna o tipo de dado")
df_clientes["qtdePontos"].dtype


# %%
