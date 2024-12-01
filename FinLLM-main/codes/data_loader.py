import json
import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd

def load_transcripts(filepath):
    with open(filepath, 'r') as f:
        dataset = [json.loads(line) for line in f]
    return dataset[::-1]  # Ensures transcripts are in chronological order

def get_stock_prices(symbol, start_date, end_date):
    prices = yf.download(symbol, start=start_date, end=end_date)
    prices = prices[['Open', 'Close']]
    prices.index = prices.index.strftime('%Y-%m-%d')
    return prices

def get_next_day_price_movement(prices, dates):
    movements = {}
    for date in dates:
        try:
            close_price = prices.loc[date]['Close']
            date_obj = datetime.strptime(date, "%Y-%m-%d")
            next_day = (date_obj + timedelta(days=1)).strftime("%Y-%m-%d")
            open_price = prices.loc[next_day]['Open']
            change = open_price / close_price - 1
            movements[date] = change
        except KeyError:
            print(f"Date {date} or the next day not found in price data.")
            continue
    return movements

def price_movement_categories(movements):
    labels = {}
    for date, change in movements.items():
        # 如果 change 是 Series，提取标量值
        if isinstance(change, pd.Series):
            change = change.item()
        # 分类
        if -0.01 <= change <= 0.01:
            labels[date] = "Flat Response (-1% to +1%)"
        elif 0.01 < change <= 0.03:
            labels[date] = "Moderate Positive (+1% to +3%)"
        elif change > 0.03:
            labels[date] = "Positive Surprise (+3% or more)"
        elif -0.03 <= change < -0.01:
            labels[date] = "Moderate Negative (-1% to -3%)"
        elif change < -0.03:
            labels[date] = "Negative Surprise (-3% or more)"
    return labels


if __name__ == "__main__":
    dataset = load_transcripts("data/goog_calls.jsonl")
    symbol = 'GOOG'
    start_date = '2014-11-01'
    end_date = '2024-11-01'
    prices = get_stock_prices(symbol, start_date, end_date)
    dates = [t["time"] for t in dataset]
    print(dates)
    movements = get_next_day_price_movement(prices, dates)
    print(movements)
    labels = price_movement_categories(movements)
    print(labels)

    
