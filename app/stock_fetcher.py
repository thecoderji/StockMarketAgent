import yfinance as yf
from datetime import datetime

class StockFetcher:
    def __init__(self):
        pass
    
    def get_stock_price(self, ticker: str) -> dict:
        """Fetch latest stock price and info using yfinance."""
        print(f"Fetching data for {ticker}")
        try:
            stock = yf.Ticker(ticker)
            # Use 1mo to ensure data availability
            hist = stock.history(period="1mo")
            if hist.empty:
                print(f"No historical data for {ticker}")
                return {"error": f"No data found for ticker {ticker}"}
            
            # Get the most recent price
            latest_price = hist['Close'].iloc[-1]
            info = stock.info
            
            # Get 50-day moving average
            hist_50d = stock.history(period="50d")
            moving_avg_50 = round(hist_50d["Close"].mean(), 2) if not hist_50d.empty else None
            
            result = {
                "ticker": ticker,
                "price": round(latest_price, 2),
                "company": info.get("longName", ticker),
                "currency": info.get("currency", "USD"),
                "timestamp": datetime.now().isoformat(),
                "moving_avg_50": moving_avg_50
            }
            print(f"Returning: {result}")
            return result
        except Exception as e:
            error = {"error": f"Failed to fetch data: {str(e)}"}
            print(f"Error: {error}")
            return error