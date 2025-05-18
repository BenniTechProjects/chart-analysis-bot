import time
from scripts.analysis import analyze_chart
from utils.telegram_utils import send_telegram_message


WATCHLIST = ["SOFI", "SPY"]

def main():
    print("Running chart bot...")
    for ticker in WATCHLIST:
        result = analyze_chart(ticker)
        message = (
            f"*{result['ticker']} Analysis*\n"
            f"Support Levels: {result['support']}\n"
            f"Resistance Levels: {result['resistance']}\n"
            f"Signal: *{result['signal']}*\n"
            f"Target Price: {result['target']}"
        )
        send_telegram_message(message)
        time.sleep(1)  # Delay to avoid rate limits

if __name__ == "__main__":
    main()