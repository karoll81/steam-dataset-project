class Game:

    # construtor da classe
    def __init__(self, name, release_date, price, recommendations):

        self.name = name
        self.release_date = release_date

        # convertendo preço para número
        if price == "":
            self.price = 0
        else:
            self.price = float(price)

        # convertendo recomendações para número
        if recommendations == "":
            self.recommendations = 0
        else:
            self.recommendations = int(recommendations)
            