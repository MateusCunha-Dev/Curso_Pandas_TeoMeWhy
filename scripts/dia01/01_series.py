import pandas as pd

idades = [17, 23, 43, 36, 41, 21, 33, 36, 38, 28]

df = pd.Series(idades)
media = df.mean()
desvio_padrao = df.std()

""" .describe() é um método de resumo estatístico que contém:

count: Quantidade de valores não nulos (útil para ver se há dados faltando).
mean: A média aritmética.
std: O desvio padrão (dispersão dos dados).
min: O menor valor encontrado.
25%: O primeiro quartil (25% dos dados são menores que este valor).
50%: A mediana (o valor central do conjunto).
75%: O terceiro quartil (75% dos dados são menores que este valor).
"""
summary_idades = df.describe()

# Z-score
print((df - media) / desvio_padrao)
print(summary_idades)
