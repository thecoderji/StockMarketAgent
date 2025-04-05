from .stock_fetcher import StockFetcher

class StockAgent:
    def __init__(self):
        self.stock_fetcher = StockFetcher()
    
    def analyze_stock(self, ticker: str) -> dict:
        """Get stock price and provide analysis with recommendation."""
        stock_data = self.stock_fetcher.get_stock_price(ticker)
        if not isinstance(stock_data, dict) or "error" in stock_data:
            return stock_data if isinstance(stock_data, dict) else {"error": "Failed to fetch stock data"}
        
        try:
            current_price = stock_data["price"]
            moving_avg_50 = stock_data.get("moving_avg_50")
            
            if moving_avg_50:
                recommendation = (
                    "BUY" if current_price < moving_avg_50 * 0.95  # 5% below MA
                    else "SELL" if current_price > moving_avg_50 * 1.05  # 5% above MA
                    else "HOLD"
                )
                analysis = (
                    f"The current price (${current_price}) is compared to the 50-day moving average "
                    f"(${moving_avg_50}). Recommendation: {recommendation}."
                )
            else:
                recommendation = "HOLD"
                analysis = (
                    f"The current price (${current_price}) is evaluated against market trends. "
                    f"Recommendation: {recommendation}. (Historical data unavailable.)"
                )
        except Exception as e:
            analysis = f"Analysis unavailable: {str(e)}"
        
        return {
            **stock_data,
            "analysis": analysis
        }