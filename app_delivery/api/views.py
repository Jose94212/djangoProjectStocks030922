from datetime import date, timedelta
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from django.shortcuts import render
from app_platforms.models import ModelPlatforms
from rest_framework import status
from rest_framework.decorators import api_view
from nsepy import get_history

# Create your views here.

share_symbols=["GLAND","HDFCBANK","TATAELXSI","TATASTEEL","TATAPOWER","DRREDDY",
                "BAJAJFINSV","TATAMOTORS","MARUTI","BOSCHLTD","NESTLEIND","SHREECEM"]

@api_view(['GET'])
def fetch_delivery_percentage(request):
    if request.method == 'GET':
        data= fetch_share_details()
        return Response(data=data,status=status.HTTP_200_OK)

def fetch_share_details(symbol=share_symbols):
    #checkiftisweekend
    days_to_minus=0
    delivery_percentage=None
    
    if date.today().strftime("%A")=="Saturday":
        days_to_minus=1
    elif date.today().strftime("%A")=="Sunday":
        days_to_minus=2
    
    #fetching all symbols details
    all_symbol_details=[]
    for i in symbol:
        data = get_history(i,start=date.today()-timedelta(days=days_to_minus+1), 
                            end=date.today()-timedelta(days=days_to_minus))
        dict_details=dict()
        temp_dict_date=dict()
        for datee,contents in data.iterrows():

            temp_dict_open_close_delivery= dict()
            for headers,values in contents.items():
                if headers in ["Open","Close","%Deliverble"]:
                    temp_dict_open_close_delivery[headers] =values
                    #delivery_percentage=values*100
            temp_dict_date[str(datee)]=temp_dict_open_close_delivery
        dict_details[i]=temp_dict_date
        print("\ndict_details:",dict_details)
        all_symbol_details.append(dict_details)
    return all_symbol_details
    #return Response({"sbi":"40"},data=delivery_percentage,status=status.HTTP_200_OK)
    #return Response({"sbi":data},status=status.HTTP_200_OK)
        

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

