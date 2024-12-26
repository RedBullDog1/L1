import requests
import json
from datetime import date, timedelta
def fetch_exchange_rates(start_date, end_date, currency_code=''):
    url = 'https://bank.gov.ua/NBU_Exchange/exchange_site'
    params = {
        'start': start_date,
        'end': end_date,
        'valcode': currency_code,
        'sort': 'exchangedate',
        'order': 'desc',
        'json': ''
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []
def display_exchange_rates(currency_code):
    today = date.today()
    last_week = today - timedelta(days=7)
    start_date = last_week.strftime('%Y%m%d')
    end_date = today.strftime('%Y%m%d')
    rates = fetch_exchange_rates(start_date, end_date, currency_code)
    if rates:
        print(f"Exchange Rates for {currency_code} (Past Week):")
        print("-" * 40)
        for rate in rates:
            print(f"Date: {rate['exchangedate']} | Rate: {rate['rate']}")
    else:
        print(f"No exchange rate data available for {currency_code}.")
display_exchange_rates('USD')