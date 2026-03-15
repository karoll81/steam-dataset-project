import csv
from game import Game


class SteamDataset:

    # construtor da classe
    def __init__(self, file_path):
        self.games = []
        self.load_data(file_path)


    # função para carregar os dados do CSV
    def load_data(self, file_path):

        with open(file_path, encoding="utf-8") as file:

            reader = csv.DictReader(file)

            for row in reader:

                # criando objeto Game
                game = Game(
                    row["Name"],
                    row["Release date"],
                    row["Price"],
                    row["Recommendations"]
                )

                # adicionando na lista
                self.games.append(game)


    # função que calcula porcentagem de jogos gratuitos e pagos
    def percentage_free_paid(self):

        free = 0
        paid = 0

        for game in self.games:

            if game.price == 0:
                free += 1
            else:
                paid += 1

        total = free + paid

        percent_free = (free / total) * 100
        percent_paid = (paid / total) * 100

        return percent_free, percent_paid

 # agora montar função que descobre qual ano teve mais jogos
    def year_with_most_games(self):

        years = {}

        for game in self.games:

            # pega apenas o ano da data
            year = game.release_date[-4:]

            if year in years:
                years[year] += 1
            else:
                years[year] = 1

        max_games = max(years.values())

        result = []

        for year in years:
            if years[year] == max_games:
                result.append(year)

        return result
         # montar função para descobrir qual jogo tem mais recomendações
    def game_with_most_recommendations(self):

        top_game = None
        max_recommendations = 0

        # percorre todos os jogos
        for game in self.games:

            if game.recommendations > max_recommendations:
                max_recommendations = game.recommendations
                top_game = game

        return top_game.name, max_recommendations