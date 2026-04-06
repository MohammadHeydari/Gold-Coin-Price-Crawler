class MarketData:

    def __init__(self, timestamp, ounce, gold18, gold24, coin_new, coin_old,
                 half_coin, quarter_coin, gram_coin):

        self.timestamp = timestamp
        self.ounce = ounce
        self.gold18 = gold18
        self.gold24 = gold24

        self.coin_new = coin_new
        self.coin_old = coin_old
        self.half_coin = half_coin
        self.quarter_coin = quarter_coin
        self.gram_coin = gram_coin