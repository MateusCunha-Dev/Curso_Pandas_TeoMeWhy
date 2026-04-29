# %%
import pandas as pd
idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39,
]

nomes = [
    "Téo", "Maria", "Jose", "Luis", "Ana",
    "Nah", "Dani", "Mah", "Fer", "Nanda",
    "Naty", "Nih", "Pedro", "Kozato", "Kozato",
]

pesos = [
    72, 48, 80, 60, 51,
    55, 65, 59, 61, 67,
    57, 73, 86, 73, 73,
]

df = pd.DataFrame()
series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)
series_pesos = pd.Series(pesos)

# %%
print("O dataframe é como um conjunto de séries (cada coluna)")
df['idades'] = series_idades
df['nomes'] = series_nomes
df['pesos'] = series_pesos
# %%
print(df)
# %%
print("\nAcessanddo um registro do DataFrame por meio do .iloc")
print(f"df.iloc[0]:\n{df.iloc[0]}")

print("\nAcessando um dado específico do DataFrame por meio do .loc")
print(f"df.iloc[0][nomes]:\n{df.iloc[0]['nomes']}")
