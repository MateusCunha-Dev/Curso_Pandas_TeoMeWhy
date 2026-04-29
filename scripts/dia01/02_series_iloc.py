# %% 
import pandas as pd

# 'idades' e 'nomes' são listas nativas
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

series_idades = pd.Series(idades)

print("--- SERIES ORIGINAL ---")
print(series_idades)


# %% - Navegação Básica e o Truque do Índice Negativo
print("\n--- ACESSO AOS DADOS ---")

# Acessando o primeiro elemento
print("Primeira idade (Lista Nativa):", idades[0])
print("Primeira idade (Series Pandas):", series_idades[0])

# Acessando o último elemento
print("Última idade (Lista Nativa usando -1):", idades[-1])
print("Última idade (Series Pandas usando iloc):", series_idades.iloc[-1])
print("No Pandas, o [-1] direto daria KeyError. Precisamos " \
        "obrigar a busca pela posição física com o .iloc")

# %% - Ordenação e a Armadilha da Posição Física vs Rótulo
print("\n--- SERIES ORDENADA ---")


series_idades_ordenada = series_idades.sort_values()

print(series_idades_ordenada) 
print("Os valores da séries estão ordenados do menor para o maior." \
      " O índice original 'viaja' junto com o valor")

print("\nBuscando o menor valor após ordenação:")
print("Idade na 1ª posição física (iloc[0]):", series_idades_ordenada.iloc[0])
print("O .iloc ignora os rótulos bagunçados e pega quem está fisicamente na linha zero agora")

# %% 4. Aplicando Índices Customizados (Nomes) e usando .loc
print("\n--- SERIES COM ÍNDICES NOMEADOS ---")

series_nomes = pd.Series(idades, index=nomes)
print(series_nomes)
print("Os números automáticos foram substituidos pelos nomes da lista 'nomes'")

print("\nBuscando idades de pessoas específicas:")
print("Pela posição física (iloc[0]):", series_nomes.iloc[0])
print("Pelo nome exato (loc['Maria']):", series_nomes.loc["Maria"])


print("\nPelo nome repetido (loc['Kozato']):")
print(series_nomes.loc["Kozato"])
print("O Kozato aparece duas vezes. O .loc vai trazer ambas as idades")
