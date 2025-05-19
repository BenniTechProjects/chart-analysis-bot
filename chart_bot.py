import sys
import os
import time
from scripts.analysis import analyze_chart
from utils.telegram_utils import send_telegram_message

# Ensure all print output appears in Railway logs
sys.stdout = sys.stderr

WATCHLIST = ["SOFI", "SPY"]

def main():
    print("🚀 Bot is starting...", flush=True)

    # Log environment variables
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    print(f"🧪 TELEGRAM_BOT_TOKEN: {bot_token}", flush=True)
    print(f"🧪 TELEGRAM_CHAT_ID: {chat_id}", flush=True)

    # Send test message
    print("📨 Sending test message to Telegram...", flush=True)
    send_telegram_message("✅ Bot deployed and ready!")

    print("🤖 Running chart analysis...", flush=True)

    for ticker in WATCHLIST:
        print(f"📊 Analyzing {ticker}...", flush=True)
        result = analyze_chart(ticker)
        print(f"✅ Result for {ticker}: {result}", flush=True)

        message = (
            f"*{result['ticker']}* Analysis\n"
            f"Support Levels: {result['support']}\n"
            f"Resistance Levels: {result['resistance']}\n"
            f"Signal: *{result['signal']}*\n"
            f"Target Price: {result['target']}"
        )

        print(f"📤 Sending message:\n{message}", flush=True)
        send_telegram_message(message)
        time.sleep(1)  # Respect rate limits

if __name__ == "__main__":
    main()
