from django.shortcuts import render
from asyncio import threads
import time
from django.test import TestCase
from nsepy import get_history
from datetime import date, datetime, timedelta
from nsepy.symbols import get_symbol_list
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def fetch_bullish_engulfing(request):
    if request.method == 'GET':
        return Response(data=fetch_bullish_shares(),status=status.HTTP_200_OK)

def fetch_previous_today(item_to_iterate):
    """will fetch previous and todays' details"""
    list_save = []
    for i, k in item_to_iterate.items():
        list_save.append(k)
    return list_save


def check_weekend():
    """
    this method will check if its a weekend or not.
    if weekend, will return days_to_minus accordingly.
    if weekday and time less than 7 pm,will return 1day to minues from current date 
    """
    # checkiftisweekend
    days_to_minus = 0
    delivery_percentage = None

    if date.today().strftime("%A") == "Saturday":
        days_to_minus = 1
    elif date.today().strftime("%A") == "Sunday":
        days_to_minus = 2
    elif (date.today().weekday() and datetime.now().strftime("%H:%M:%S") < "19:00:00"):
        days_to_minus = 1
    return days_to_minus


def fetch_penny_stocks():
    """get penny stockssymols from .txt file
        and saves in the variable penny_stocks
    """
    penny_stocks = []
    try:
        with open(r'pennystocks.txt', 'r') as fp:
            for line in fp:
                x = line[:-1]
                # add current item to the list
                penny_stocks.append(x)
    except FileNotFoundError as e:
        print(e)
    return penny_stocks


def fetch_bullish_shares():
    symbolss = get_symbol_list().SYMBOL
    penny_stocks = fetch_penny_stocks()
    response_engulfing =[]

    if (penny_stocks and len(penny_stocks) > 0):
        for symbol in symbolss:
            if symbol not in penny_stocks:
                try:
                    print("checking symbol:",symbol)
                    days_to_minus = check_weekend()

                    # start=a day before the current date
                    # end = current date
                    try:
                        data = get_history(symbol, start=date.today() -
                                            timedelta(days=days_to_minus+1),
                                            end=date.today()-timedelta(days=days_to_minus))
                    except Exception:
                        print("chill!!!")
                    previous_today_low = fetch_previous_today(data["Low"])
                    previous_today_high = fetch_previous_today(data["High"])
                    previous_today_close = fetch_previous_today(data["Close"])
                    previous_today_open = fetch_previous_today(data["Open"])

                # 1st condition: previous day should be in red
                # 2nd condition: current day's open should be less than previous day's close
                #               and current day's close should be greater than previous day's open
                    if (previous_today_open[0] > previous_today_close[0] and
                            previous_today_open[1] < previous_today_close[0] and
                            previous_today_close[1] > previous_today_open[0]):
                        print("Syombol=%s bull engulf" % symbol)
                        response_engulfing.append(symbol)
                except Exception:
                    print("chill2!!!")
    else:
        raise Exception("\npenny_stocks is none or empty")
    return response_engulfing