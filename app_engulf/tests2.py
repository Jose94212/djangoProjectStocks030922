

from nsepy import get_history
from datetime import date, datetime, timedelta
from nsepy.symbols import get_symbol_list
from api.views import fetch_bullish_shares

symbolss = get_symbol_list().SYMBOL
# print(type(symbolss))
# if  symbolss.:
#     print("\nTrue")

#print(data.to_dict().get("Symbol"))
#print(type(data))
# for i,k in data.items():
#     print("\n",i,k)

penny_stocks=[]


# for i in symbolss:
#     try:
#         try:
#             data= get_history(i,start=date.today()-timedelta(days=2),end=date.today()-timedelta(days=2))
#         except Exception:
#             print("\n","get_history")
#         for ii in data["Low"]:
#             if int(ii)<=250:
#                 for k in data["Symbol"]:
#                     print(k,ii)
#                     penny_stocks.append(k)
#             # else:
#             #     print(".",end =" ")
#     except Exception:
#         print("\n","symbols")

# with open(r'pennystockss.txt', 'w') as fp:
#     fp.write('\n'.join(penny_stocks))

# with open(r'pennystockss.txt', 'w') as fp:
#     fp.write('\n'.join(penny_stocks))

# try:
#     #fd=open('pennystocksss.txt')
#     with open(r'pennystocksss.txt', 'r') as fp:
#         print(fp)
# except Exception as e:
#     print("\nFilenotFound!","\nException",e)

fetch_bullish_shares()