# %%
import pandas as pd
from IPython.display import display

PATH = '../../data/clientes.csv'
df = pd.read_csv(PATH, sep=";")
df.to_csv("clientes.csv", index=False)
display(df.head(10))

# %%
df.to_parquet("clientes.parquet", index=False) #é um arquivo binário
df_2 = pd.read_parquet("clientes.parquet")
display(df_2.head(10))

# %%
df.to_excel("clientes.xlsx", index=False)
df_3 = pd.read_excel("clientes.xlsx")
display(df_3.head(10))

# %%
