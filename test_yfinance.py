import yfinance as yf

ticker = "AAPL"
stock = yf.Ticker(ticker)
hist = stock.history(period="5d")

print(f"History for {ticker}:")
print(hist)

ticker = "RELIANCE.NS"
stock = yf.Ticker(ticker)
hist = stock.history(period="5d")

print(f"History for {ticker}:")
print(hist)