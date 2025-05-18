import os
import pandas as pd
import time
from scripts.analysis import analyze_ticker
from utils.telegram import send_telegram_message

WATCHLIST_FILE = 'watchlist.csv'
INTERVAL = 15 * 60  # 15 minutes

def load_watchlist():
    if os.path.exists(WATCHLIST_FILE):
        return pd.read_csv(WATCHLIST_FILE)['ticker'].dropna().tolist()
    else:
        return []

def main():
    send_telegram_message("✅ Chart Bot is now running on Railway.")
    while True:
        tickers = load_watchlist()
        for ticker in tickers:
            try:
                print(f"🔍 Analyzing {ticker}...")
                result = analyze_ticker(ticker)
                send_telegram_message(result)
            except Exception as e:
                send_telegram_message(f"⚠️ Error analyzing {ticker}: {e}")
        print(f"⏱️ Sleeping for {INTERVAL / 60} minutes...\n")
        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()

