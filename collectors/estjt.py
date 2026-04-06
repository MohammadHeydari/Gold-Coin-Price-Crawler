import urllib.request
import re
import html
import datetime

from models.price import MarketData

def fa_to_en(s):
    """Convert Persian/ Arabic digits to English"""
    trans = str.maketrans("۰۱۲۳۴۵۶۷۸۹٫٬", "0123456789..")
    return s.translate(trans).replace(" ", "")

def extract_number(text):
    """Extract numbers from text"""
    text = html.unescape(text)
    text = re.sub(r"[^\d۰-۹]", "", text)
    return fa_to_en(text)

def get_price():
    """Extract data from estjt.ir"""
    url = "https://www.estjt.ir/"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        req = urllib.request.Request(url, headers=headers)
        html_data = urllib.request.urlopen(req, timeout=20).read().decode("utf-8", errors="ignore")

        #extract rows with regex
        rows = re.findall(r'<td class="name">(.*?)</td>\s*<td class="price">(.*?)</td>', html_data, re.S)

        data_map = {}
        for name, price in rows:
            name = name.strip()
            price = extract_number(price)

            if "۱۸" in name or "18" in name:
                data_map["gold18"] = price
            elif "۲۴" in name or "24" in name:
                data_map["gold24"] = price
            elif "انس" in name or "اونس" in name:
                data_map["ounce"] = price
            elif "جدید" in name:
                data_map["coin_new"] = price
            elif "قدیم" in name:
                data_map["coin_old"] = price
            elif "نیم" in name:
                data_map["half_coin"] = price
            elif "ربع" in name:
                data_map["quarter_coin"] = price
            elif "گرم" in name:
                data_map["gram_coin"] = price

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return MarketData(
            timestamp=timestamp,
            ounce=data_map.get("ounce"),
            gold18=data_map.get("gold18"),
            gold24=data_map.get("gold24"),
            coin_new=data_map.get("coin_new"),
            coin_old=data_map.get("coin_old"),
            half_coin=data_map.get("half_coin"),
            quarter_coin=data_map.get("quarter_coin"),
            gram_coin=data_map.get("gram_coin"),
        )

    except Exception as e:
        print("Error in data crawling: ", e)
        return None