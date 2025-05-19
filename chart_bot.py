import time
import os
from scripts.analysis import analyze_chart
from utils.telegram_utils import send_telegram_message

WATCHLIST = ["SOFI", "SPY"]

def main():
    print("🟢 Bot is running...")
    print("📤 Telegram Bot Token:", os.getenv("TELEGRAM_BOT_TOKEN"))
    print("📤 Telegram Chat ID:", os.getenv("TELEGRAM_CHAT_ID"))

    for ticker in WATCHLIST:
        print(f"📊 Analyzing {ticker}...")
        result = analyze_chart(ticker)
        print("✅ Result:", result)

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

if __name__ == "__main__":
    main()
