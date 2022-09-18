from datetime import date, datetime, timedelta
from http.client import HTTPResponse
from logging import raiseExceptions
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from django.shortcuts import render
from app_platforms.models import ModelPlatforms
from rest_framework import status
from rest_framework.decorators import api_view
from nsepy import get_history
from nsepy.symbols import get_symbol_list

# Create your views here.

custom_share_symbols = ["GLAND", "HDFCBANK", "TATAELXSI", "TATASTEEL", "TATAPOWER", "DRREDDY",
                 "BAJAJFINSV", "TATAMOTORS", "MARUTI", "BOSCHLTD", "NESTLEIND", "SHREECEM"]


@api_view(['GET'])
def fetch_delivery_percentage(request):
    """
    will fetech the dlivery %
    """
    if request.method == 'GET':
        data = fetch_share_details()
        return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET'])
def fetch_custom_shares_delivery_details(request):
    if request.method == 'GET':
        data = fetch_share_details(custom_share_symbols)
        return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET'])
def fetch_delivery_greater_than_yesterday(request):
    if request.method == 'GET':
        data = fetch_share_details()
        return Response(data=identify_delivery_greater_than_yesterday(data),
                status=status.HTTP_200_OK)
@api_view(['GET'])
def fetch_custom_shares_delivery_greater_than_yesterday(request):
    if request.method == 'GET':
        data = fetch_share_details(custom_share_symbols)
        return Response(data=identify_delivery_greater_than_yesterday(data),
                status=status.HTTP_200_OK)

def identify_delivery_greater_than_yesterday(data):
    list_delivery_greater_than_yesterday = []
    if data:
        print("\n\tchecking for delivery greater than yesterday...")
        for shares in data:
            try:
                for share_details in shares.values():
                    temp_deliverable=[]
                    for values in share_details.values():
                        temp_deliverable.append(values.get("%Deliverble"))
                    if temp_deliverable[1]>temp_deliverable[0]:
                        print("share delivery'%' greater than yesterday:",shares)
                        list_delivery_greater_than_yesterday.append(shares)
            except Exception:
                pass
    else:
        return None
    return list_delivery_greater_than_yesterday

def fetch_share_details(symboll=None):
    """
    this method will get the delivery %
    """
    # checkiftisweekend
    days_to_minus = 0
    delivery_percentage = None

    if date.today().strftime("%A") == "Saturday":
        days_to_minus = 1
    elif date.today().strftime("%A") == "Sunday":
        days_to_minus = 2
    elif (date.today().weekday() and datetime.now().strftime("%H:%M:%S")<"19:00:00"):
        days_to_minus = 1

    if symboll is None:
        penny_stocks = fetch_penny_stocks()
        symboll = [i for i in get_symbol_list().SYMBOL if i not in penny_stocks]

    # fetching all symbols details
    all_symbol_details = []
    for i in symboll:
        data = get_history(i, start=date.today()-timedelta(days=days_to_minus+1),
                           end=date.today()-timedelta(days=days_to_minus))

        dict_details = dict()
        temp_dict_date = dict()

        for datee, contents in data.iterrows():
            temp_dict_open_close_delivery = dict()

            for headers, values in contents.items():
                if headers in ["Open", "Close", "%Deliverble",""]:
                    temp_dict_open_close_delivery[headers] = values
                    # delivery_percentage=values*100
            temp_dict_date[str(datee)] = temp_dict_open_close_delivery
        dict_details[i] = temp_dict_date
        print("\ndict_details:", dict_details)
        all_symbol_details.append(dict_details)
    return all_symbol_details
    # return Response({"sbi":"40"},data=delivery_percentage,status=status.HTTP_200_OK)
    # return Response({"sbi":data},status=status.HTTP_200_OK)


@api_view(['GET'])
def get_sbi_delivery(request):
    if request.method == 'GET':
        pass
    #     all_platforms = ModelPlatforms.objects.all()
    #     serializer=PlatformSerializer(all_platforms,many=True)
    #     return Response(serializer.data,status=status.HTTP_200_OK)

    # elif request.method == 'POST':
    #     serializer = PlatformSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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