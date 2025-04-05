# Stock Market AI Agent

A simple, powerful tool to analyze stocks using Python, FastAPI, and Yahoo Finance (`yfinance`). Built for a **Python Backend LLM Assessment**, it fetches real-time stock prices and gives buy/sell/hold recommendations for US and Indian markets.

## What It Does

- Fetches stock details (price, company name, currency) for tickers like "AAPL" (Apple) and "RELIANCE.NS" (Reliance Industries).
- Analyzes stocks using the 50-day moving average to suggest "BUY", "SELL", or "HOLD".
- Provides a fast, easy-to-use API with clear responses.

## Features

- **Global Stocks**: Works for US (e.g., "AAPL", "TSLA") and Indian (e.g., "RELIANCE.NS") stocks.
- **FastAPI**: Runs a modern API with Swagger UI at `/docs`.
- **Detailed Output**: Includes price, company, currency, 50-day average, and recommendation.
- **Simple Code**: Easy to understand and extend.

## Project Structure

StockMarketAgent/
├── app/
│ ├── stock_fetcher.py # Gets stock data
│ ├── agent.py # Analyzes and recommends
│ ├── api.py # API setup
├── main.py # Runs the app
├── requirements.txt # Dependencies
├── .env # Port settings
└── README.md # This file

## Setup

1. **Clone the Repo**:
   ```bash
   git clone https://github.com/your-username/StockMarketAgent.git
   cd StockMarketAgent
   Setup Virtual Environment:
   bash
   ```

python -m venv venv
venv\Scripts\activate # Windows

# source venv/bin/activate # macOS/Linux

Install Dependencies:
pip install -r requirements.txt

Set Port (in .env):
PORT=8000

Run the App:
python main.py

API runs at http://localhost:8000.

How to Use
API Endpoint: POST /stock
Request: Send a ticker in JSON.
Powershell
Invoke-WebRequest -Uri "http://localhost:8000/stock" -Method Post -Headers @{"Content-Type"="application/json"} -Body '{"ticker":"COMPANY_STOCK_NAME"}' | Select-Object -ExpandProperty Content | ConvertFrom-Json
Response Example (AAPL):

ticker: AAPL
price: 199.88
company: Apple Inc.
currency: USD
timestamp: 2025-04-05T12:00:00.123456
moving_avg_50: 228.50
analysis: The current price ($199.88) is compared to the 50-day moving average ($228.50). Recommendation: BUY.

Try These Tickers
US: "AAPL", "TSLA"
India: "RELIANCE.NS", "TCS.NS"

Example Outputs-
AAPL:
ticker: AAPL
price: 199.88
company: Apple Inc.
currency: USD
moving_avg_50: 228.50
analysis: The current price ($199.88) is compared to the 50-day moving average ($228.50). Recommendation: BUY.

RELIANCE.NS:
ticker: RELIANCE.NS
price: 1245.45
company: Reliance Industries Limited
currency: INR
moving_avg_50: 1270.00
analysis: The current price ($1245.45) is compared to the 50-day moving average ($1270.00). Recommendation: BUY.


# Requirements
Python 3.10+
Internet connection for yfinance
Windows/macOS/Linux
Troubleshooting
No Data: Check ticker (e.g., "RELIANCE.NS", not "RELIANCE") and internet.
Server Error: Verify requirements.txt install and run from project root.
