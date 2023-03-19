# https://www.youtube.com/watch?v=tG8PPne7ef0
# https://www.alphavantage.co/

"""
Use alphavantage API to get stock data and plot it in a graph using matplotlib
"""


import requests
# import pandas as pd

# API_KEY = 'YOUR_API_KEY'
API_KEY = 'RTART83NP1R7G8X'
STOCK_SYMBOL = 'MSFT'


def get_daily_stock_data(symbol: str):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data


def main():
    data = get_daily_stock_data(STOCK_SYMBOL)
    print(data)
    pass

if __name__ == "__main__":
    main()


## WARNINGS
# {'Information': 'Thank you for using Alpha Vantage! This is a premium endpoint. 
# You may subscribe to any of the premium plans at https://www.alphavantage.co/premium/ to instantly unlock all premium endpoints'}
