import csv
import os

FILE = "data/gold_price.csv"

def save(data):

    file_exists = os.path.isfile(FILE)

    with open(FILE, "a", newline="", encoding="utf-8") as f:

        writer = csv.writer(f)

        if not file_exists:
            writer.writerow([
                "timestamp",
                "ounce",
                "gold18",
                "gold24",
                "coin_new",
                "coin_old",
                "half_coin",
                "quarter_coin",
                "gram_coin"
            ])

        writer.writerow([
            data.timestamp,
            data.ounce,
            data.gold18,
            data.gold24,
            data.coin_new,
            data.coin_old,
            data.half_coin,
            data.quarter_coin,
            data.gram_coin
        ])

