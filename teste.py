from steam_dataset import SteamDataset


print("---Análise de dados do dataset de jogos da Steam---")
print("Este programa realiza algumas análises a partir de um dataset de jogos da Steam.")
print("O objetivo é calcular o percentual de jogos gratuitos e pagos,")
print("identificar o ano com maior número de lançamentos")
print("e encontrar o jogo com maior número de recomendações.")
print("Também é feita uma verificação utilizando uma amostra de 20 jogos.\n")

# montando o visual dos resultados que serão exibidos 
print("\n=== DATASET COMPLETO ===")

dataset = SteamDataset("steam_games.csv")

print("Quantidade de jogos carregados:", len(dataset.games))

free, paid = dataset.percentage_free_paid()
print(f"Porcentagem de jogos gratuitos: {free:.2f}%")
print(f"Porcentagem de jogos pagos: {paid:.2f}%")

years = dataset.year_with_most_games()
print("Ano com mais jogos lançados:", years)

name, rec = dataset.game_with_most_recommendations()
print("Jogo com mais recomendações:", name)
print("Número de recomendações:", rec)


print("\n=== AMOSTRA DE 20 JOGOS ===")

sample = SteamDataset("steam_games_sample.csv")

print("Quantidade de jogos carregados:", len(sample.games))

free, paid = sample.percentage_free_paid()
print(f"Porcentagem de jogos gratuitos: {free:.2f}%")
print(f"Porcentagem de jogos pagos: {paid:.2f}%")

years = sample.year_with_most_games()
print("Ano com mais jogos lançados:", years)

name, rec = sample.game_with_most_recommendations()
print("Jogo com mais recomendações:", name)
print("Número de recomendações:", rec)