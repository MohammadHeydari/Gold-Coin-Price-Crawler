import csv
import matplotlib.pyplot as plt
from datetime import datetime

FILE = "data/gold_price.csv"


def load_data():

    t = []
    ounce = []
    gold18 = []
    gold24 = []
    coin_new = []
    coin_old = []
    half_coin = []
    quarter_coin = []
    gram_coin = []

    with open(FILE, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)

        for row in reader:
            if len(row) < 9:
                continue

            try:
                t.append(datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S"))

                ounce.append(int(row[1]))
                gold18.append(int(row[2]))
                gold24.append(int(row[3]))
                coin_new.append(int(row[4]))
                coin_old.append(int(row[5]))
                half_coin.append(int(row[6]))
                quarter_coin.append(int(row[7]))
                gram_coin.append(int(row[8]))

            except:
                continue

    return t, ounce, gold18, gold24, coin_new, coin_old, half_coin, quarter_coin, gram_coin


def plot():

    t, ounce, g18, g24, cnew, cold, half, quarter, gram = load_data()

    fig, axes = plt.subplots(3, 1, figsize=(14, 10), sharex=True)

    # -------------------
    # Plot 1: Gold
    # -------------------
    axes[0].plot(t, g18, label="Gold 18K")
    axes[0].plot(t, g24, label="Gold 24K")
    axes[0].set_title("Gold Prices")
    axes[0].legend()
    axes[0].grid(True)

    # -------------------
    # Plot 2: Coins
    # -------------------
    axes[1].plot(t, cnew, label="Coin New")
    axes[1].plot(t, cold, label="Coin Old")
    axes[1].plot(t, half, label="Half Coin")
    axes[1].plot(t, quarter, label="Quarter Coin")
    axes[1].plot(t, gram, label="Gram Coin")

    axes[1].set_title("Coin Prices")
    axes[1].legend()
    axes[1].grid(True)

    # -------------------
    # Plot 3: Ounce
    # -------------------
    axes[2].plot(t, ounce, label="Ounce Price", color="black")

    axes[2].set_title("International Gold (Ounce)")
    axes[2].legend()
    axes[2].grid(True)

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("visualization/output/chart.png", dpi=150)

    plt.show()


if __name__ == "__main__":
    plot()