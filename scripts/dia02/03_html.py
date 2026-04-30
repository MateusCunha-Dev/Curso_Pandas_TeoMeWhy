# %%
import pandas as pd

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"
url_2 = "https://www.mat.ufmg.br/futebol/classificacao-geral_seriea"
disfarce = {'User-Agent': 'Mozilla/5.0'} # disfarce para evitar 'HTTP Error 403: Forbidden'

dfs = pd.read_html(url, storage_options=disfarce)
df_uf = dfs[1]
df_uf.to_csv("uf.csv", sep=";", index=False)


# %%
print("\nUsando a URL da classificação do Brasileirão 2026 serie A:")
dfs_2 = pd.read_html(url_2, storage_options=disfarce)
df_br2026 = dfs_2[0]
df_br2026.to_csv("br_2026.csv", index=False)


# %%
