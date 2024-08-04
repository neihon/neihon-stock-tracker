import requests

apiKey= ()
def get_stock(entry):
    url = (f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={entry}&apikey={apiKey}")
    #url= (f"https://query1.finance.yahoo.com/v8/finance/chart/{entry}")
    url_data = requests.get(url)
    data = url_data.json()
    return get_data(data)
    
def get_data(data):
    ticker = data["Meta Data"]["2. Symbol"]
    daily_prices = data["Time Series (Daily)"]
    latest_date = list(daily_prices.keys())[0]
    prices = daily_prices[latest_date]
    open_price = prices["1. open"]
    close_price = prices["4. close"]
    stock_data = [ticker, open_price, close_price]
    return stock_data
