from typing import Optional

from fastapi import FastAPI
import requests
from datetime import datetime
import aiohttp
import asyncio

app = FastAPI()

# Pending to add tests


async def req(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            r = await resp.json(content_type=None)
            print(r)
            return r

# List of all currencies


@app.get("/")
def list_all_currencies():
    return asyncio.run(req(
        'https://free.currconv.com/api/v7/currencies?apiKey=afa05cb7a89854314753'))


# Convert Endpoint, Sample: localhost:8000/convert/KWR/INR


@app.get("/convert/{from_currency}/{to_currency}")
def convert(from_currency: str = 'USD_PHP', to_currency: str = 'PHP_USD'):
    if '_PHP' not in from_currency:
        from_currency = from_currency+'_PHP'
    if 'PHP_' not in to_currency:
        to_currency = 'PHP_'+to_currency
    return asyncio.run(req(
        'https://free.currconv.com/api/v7/convert?q='+from_currency+','+to_currency+'&compact=ultra&apiKey=afa05cb7a89854314753'))


# Historic Conversion Endpoint, Sample: localhost:8000/historic/KWR/INR/2021-08-12


@ app.get("/historic/{from_currency}/{to_currency}/{from_date}")
def historic(from_date: str = '2021-08-03', from_currency: str = 'USD_PHP', to_currency: str = 'PHP_USD'):
    if '_PHP' not in from_currency:
        from_currency = from_currency+'_PHP'
    if 'PHP_' not in to_currency:
        to_currency = 'PHP_'+to_currency
    return asyncio.run(req(
        'https://free.currconv.com/api/v7/convert?q='+from_currency+','+to_currency+'&compact=ultra&date='+from_date+'&apiKey=afa05cb7a89854314753'))
