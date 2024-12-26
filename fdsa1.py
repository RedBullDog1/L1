import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


def fetch_exchange_rate(currency_code, date):
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={currency_code}&date={date}&json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data:
            return data[0]["rate"]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {currency_code} on {date}: {e}")
    return None


def plot_exchange_rate(currency_code, days):
    today = datetime.now()
    dates = [(today - timedelta(days=i)).strftime("%Y%m%d") for i in range(days)]
    formatted_dates = [(today - timedelta(days=i)).strftime("%d.%m") for i in reversed(range(days))]

    rates = []
    for date in reversed(dates):
        rate = fetch_exchange_rate(currency_code, date)
        rates.append(rate)
    plt.figure(figsize=(10, 6))
    plt.plot(formatted_dates, rates, marker="o", linestyle="-", color="blue", label=f"Exchange Rate ({currency_code})")
    plt.title(f"Exchange Rate Trend for {currency_code} Over the Last {days} Days", fontsize=16)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Rate (UAH)", fontsize=12)
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.legend(fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
plot_exchange_rate("EUR", 7)
