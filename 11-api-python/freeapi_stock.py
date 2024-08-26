import requests

def fetchStock():
    url = "https://api.freeapi.app/api/v1/public/stocks?page=1&limit=2&inc=Symbol%2CName%2CMarketCap%2CCurrentPrice&query=tata"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        stockData = data["data"]["data"]
        stocks = []
        
        for stock in stockData:
            stock_info = {
                "Symbol": stock.get("Symbol"),
                "Name": stock.get("Name"),
                "MarketCap": stock.get("MarketCap")
            }
            stocks.append(stock_info)
        
        if len(stocks) >= 2:
            return stocks
        else:
            raise Exception("Not enough data returned")
    else:
        raise Exception("Failed to fetch data")

# Example usage
def main():
    try:
        stocks = fetchStock()
        for i, stock in enumerate(stocks, start=1):
            print(f"Stock {i}:", stock)
    except Exception as e:
     print(e)

if __name__ == "__main__":
    main()