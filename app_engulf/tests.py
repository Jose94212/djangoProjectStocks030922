
from asyncio import threads
import time
from django.test import TestCase
from nsepy import get_history
from datetime import date, datetime, timedelta
from nsepy.symbols import get_symbol_list

# import pandas as pd
# import io
# import requests
# url = 'https://www.niftyindices.com/IndexConstituent/ind_nifty50list.csv'
# s = requests.get(url).content
# df = pd.read_csv(io.StringIO(s.decode('utf-8')), on_bad_lines='skip')
# #df.Symbol
# #print(df.Symbol)

# get penny stockssymols from .txt file
penny_stocks=[]
with open(r'pennystocks.txt', 'r') as fp:
    for line in fp:
        x = line[:-1]
        # add current item to the list
        penny_stocks.append(x)

if len(penny_stocks)>0:
    print("redfrompennystocks!")

symbolss = get_symbol_list().SYMBOL
# for i,j in enumerate(symbolss):
#     if i<500:
#         print(i,j)


# # Create your tests here.
# share_symbols = ["GLAND", "HDFCBANK", "TATAELXSI", "TATASTEEL", "TATAPOWER", "DRREDDY","THERMAX",
#                  "BAJAJFINSV", "TATAMOTORS", "MARUTI", "BOSCHLTD", "NESTLEIND", "SHREECEM"]

# # data = get_history("THERMAX",start=date.today()-timedelta(days=1),end=date.today())

def fetch_previous_today(item_to_iterate):
    list_save = []
    for i, k in item_to_iterate.items():
        list_save.append(k)
    return list_save

# # previous_today_low= fetch_previous_today(data["Low"])
# # previous_today_high= fetch_previous_today(data["High"])
# # previous_today_close= fetch_previous_today(data["Close"])
# # previous_today_open= fetch_previous_today(data["Open"])


# # print(previous_today_low)
# # print(previous_today_high)
# # print(previous_today_close)
# # print(previous_today_open)


for i, symbol in enumerate(symbolss):
    print("goingfor:",symbol)
    if symbol not in penny_stocks:
        print("not in penny_stocks!")
        try:
            data = get_history(symbol, start=date.today() -
                               timedelta(days=2), end=date.today()-timedelta(days=1))

            previous_today_low = fetch_previous_today(data["Low"])
            if previous_today_low[0] <= 150:
                continue
            previous_today_high = fetch_previous_today(data["High"])
            previous_today_close = fetch_previous_today(data["Close"])
            previous_today_open = fetch_previous_today(data["Open"])

        # 1st condition: previous day should be in red
            if (previous_today_open[0] > previous_today_close[0] and previous_today_open[1] < previous_today_close[0]
                    and previous_today_close[1] > previous_today_open[0]):
                print(i, "Syombol=%s bull engulf" % symbol)
        except Exception:
            pass
