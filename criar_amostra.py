import csv
import random

# arquivo original
arquivo_original = "steam_games.csv"

# arquivo da amostra
arquivo_amostra = "steam_games_sample.csv"

with open(arquivo_original, encoding="utf-8") as f:
    reader = list(csv.reader(f))

# separa o cabeçalho
header = reader[0]
dados = reader[1:]

# pega 20 jogos aleatórios
amostra = random.sample(dados, 20)

with open(arquivo_amostra, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(amostra)

print("Arquivo de amostra criado com 20 jogos!")