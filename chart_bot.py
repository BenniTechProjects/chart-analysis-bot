import os
import time
from dotenv import load_dotenv
from scripts.analysis import analyze_chart
from utils.telegram_utils import send_telegram_message

print("✅ chart_bot.py loaded.")
print("✅ Imports successful.")

# Load variables from .env
load_dotenv()

WATCHLIST = ["SOFI", "SPY"]

def main():
    print("🚀 Entering main()...")
    print("🤖 Bot is running...")

    bot_token = os.getenv("TELEGRAM_BOT_TOKEN", "MISSING_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID", "MISSING_ID")

    print(f"🔐 Telegram Bot Token: {bot_token}")
    print(f"💬 Telegram Chat ID: {chat_id}")

    for ticker in WATCHLIST:
        print(f"📈 Analyzing {ticker}...")
        result = analyze_chart(ticker)
        print(f"🧪 Raw result for {ticker}: {result}")

        if result is None:
            print(f"⚠️ No result for {ticker}, skipping.")
            continue

        print(f"✅ Result: {result}")

        message = (
            f"*{result['ticker']} Analysis*\n"
            f"Support Levels: {result['support']}\n"
            f"Resistance Levels: {result['resistance']}\n"
            f"Signal: *{result['signal']}*\n"
            f"Target Price: {result['target']}"
        )

        print(f"📤 Sending message:\n{message}")
        send_telegram_message(message)
        time.sleep(1)

    # TEMP TEST
    print("📢 Sending test deployment message...")
    send_telegram_message("✅ Bot deployed successfully and Telegram is working!")

if __name__ == "__main__":
    main()
    print("💤 Entering sleep loop to keep container alive...")
    while True:
        time.sleep(60)
