import os
import time
from scripts.analysis import analyze_chart
from utils.telegram_utils import send_telegram_message

WATCHLIST = ["SOFI", "SPY"]

def run_bot_once():
    print("🤖 Bot running once...")
    print("📡 Telegram Bot Token:", os.getenv("TELEGRAM_BOT_TOKEN"))
    print("🆔 Telegram Chat ID:", os.getenv("TELEGRAM_CHAT_ID"))

    for ticker in WATCHLIST:
        print(f"🔍 Analyzing {ticker}...")
        result = analyze_chart(ticker)
        print(f"✅ Result for {ticker}:", result)

        message = (
            f"*{result['ticker']} Analysis*\n"
            f"Support Levels: {result['support']}\n"
            f"Resistance Levels: {result['resistance']}\n"
            f"Signal: *{result['signal']}*\n"
            f"Target Price: {result['target']}"
        )

        print(f"📨 Sending message:\n{message}")
        send_telegram_message(message)
        time.sleep(1)

def main():
    while True:
        run_bot_once()
        print("🕒 Sleeping 60 seconds before next run...")
        time.sleep(60)  # Delay between cycles

if __name__ == "__main__":
    main()
