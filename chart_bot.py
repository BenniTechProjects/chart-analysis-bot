import os
import time
from utils.telegram_utils import send_telegram_message

print("✅ chart_bot.py loaded.")
print("✅ Imports successful.")

WATCHLIST = ["TEST"]

def main():
    print("🤖 Bot is running...")

    bot_token = os.getenv("TELEGRAM_BOT_TOKEN", "MISSING_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID", "MISSING_ID")

    print("🟢 Telegram Bot Token:", bot_token)
    print("🟢 Telegram Chat ID:", chat_id)

    for ticker in WATCHLIST:
        print(f"📈 Analyzing {ticker}...")

        result = {
            "ticker": ticker,
            "support": [5.0, 4.5, 4.0],
            "resistance": [6.0, 6.5, 7.0],
            "signal": "CALL",
            "target": 6.5
        }

        print(f"✅ Result: {result}")

        message = (
            f"*{result['ticker']}* Analysis\n"
            f"Support Levels: {result['support']}\n"
            f"Resistance Levels: {result['resistance']}\n"
            f"Signal: *{result['signal']}*\n"
            f"Target Price: {result['target']}"
        )

        print(f"📤 Sending message:\n{message}")
        send_telegram_message(message)
        time.sleep(1)

if __name__ == "__main__":
    print("🔁 Entering main()...")
    main()
