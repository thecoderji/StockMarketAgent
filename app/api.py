from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .agent import StockAgent

app = FastAPI(
    title="Stock Market AI Agent",
    description="API for fetching stock prices and analysis",
    version="1.0.0"
)

class StockRequest(BaseModel):
    ticker: str

stock_agent = StockAgent()

@app.get("/")
async def root():
    return {"message": "Welcome to Stock Market AI Agent"}

@app.post("/stock")
async def get_stock_analysis(request: StockRequest):
    """Get stock price and analysis for given ticker."""
    result = stock_agent.analyze_stock(request.ticker.upper())
    
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    
    return result