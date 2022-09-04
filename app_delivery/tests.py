from django.test import TestCase
from nsepy import get_history
from nsepy import symbols
from datetime import date, datetime, timedelta

# def fetch_delivery_percentatge():
#     #checkiftisweekend
#     days_to_minus=0
    
#     if date.today().strftime("%A")=="Saturday":
#         days_to_minus=1
#     elif date.today().strftime("%A")=="Sunday":
#         days_to_minus=2
    
#     data = get_history("SBIN",start=date.today()-timedelta(days=days_to_minus), 
#                         end=date.today()-timedelta(days=days_to_minus))
    
#     for i,k in data.iterrows():
#         print("\ni=",i)
#         for ii,kk in k.items():
#             print("\n iam here")
#             if ii == "%Deliverble":
#                 print("\n delivery %:",kk)
#                 break
        

    
    
# Create your tests here.
def test_abc():
    print("n testingg!!!")
    data = get_history("SBIN",start=date(2022,9,2), end=date.today())
    #data = get_history("SBIN",start=date.today(), end=date.today())
    #print(data)
    #print(type(data))
    print("\ndate=",date.today().strftime("%A"))
    print("\n yesterday date",date.today()-timedelta(days=1))

    # for i,k in data.iterrows():
    #     print("\ni=",k)
    #     for ii,kk in k.items():
    #         print("\nKey",ii,"value",kk)

#test_abc()
#fetch_delivery_percentatge()

ds={"open":123, "close":123}
dicdate={}
share={}

resp= {
        "share_name":{
                    "today":{
                            "open":123,
                            "close":134,
                            "delivey":34
                        },
                    "yesterday":{
                                "open":123, 
                                "close":134, 
                                "delivey":34
                            }
                    }
        }

print("resp type=",type(resp))
import json
data=json.dumps(resp)
ds["delivey"]=34
print("\nresp:",ds)
print("\ndicdate",dicdate)
dicdate["today"]=ds
print("\ndicdate",dicdate)
dicdate["yesterday"]=ds
share["sbare_name"]=dicdate
print("\n",share)