import time
from collectors.estjt import get_price
from storage.csv_storage import save

while True:

    data = get_price()

    if data:
        save(data)
        print("data saved!")

    time.sleep(60)

