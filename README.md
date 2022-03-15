# My Quick FastAPI Sample

# Prerequisites
- Python3
- FastAPI
- aiohttp
- requests
- asyncio

# Instructions to start
```
pip install -r requirements.txt
uvicorn main:app --reload
```
open in a web browser http://localhost:8000/docs
http://localhost:8000/redoc

# URLS
- / 
Lists all currencies

- /convert/USD/GBP
Converts from one currency to another
Parameters /from_currency/to_currency

- /historic/USD/INR/2021-05-10
Historic of Currency Exchange
Parameters /from_currency/to_currency/historical_date
