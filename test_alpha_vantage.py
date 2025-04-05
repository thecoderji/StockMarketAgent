import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
ticker = "TSLA"  # Changed to TSLA

url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={api_key}"
response = requests.get(url)
data = response.json()

print(f"Status Code: {response.status_code}")
print(f"Response: {data}")