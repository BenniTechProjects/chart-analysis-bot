import os
import sys
import time
from scripts.analysis import analyze_chart
from utils.telegram_utils import send_telegram_message

WATCHLIST = ["SOFI", "SPY"]

def main():
    print("🤖 Bot is running...", flush=True)
    
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    print(f"📡 Telegram Bot Token: {token}", flush=True)
    print(f"🆔 Telegram Chat ID: {chat_id}", flush=True)

    for ticker in WATCHLIST:
        print(f"🔍 Analyzing {ticker}...", flush=True)
        try:
            result = analyze_chart(ticker)
            print(f"✅ Result for {ticker}:", result, flush=True)

            message = (
                f"*{result['ticker']} Analysis*\n"
                f"Support Levels: {result['support']}\n"
                f"Resistance Levels: {result['resistance']}\n"
                f"Signal: *{result['signal']}*\n"
                f"Target Price: {result['target']}"
            )
            print(f"📨 Sending message:\n{message}", flush=True)
            send_telegram_message(message)

        except Exception as e:
            print(f"❌ Error analyzing {ticker}: {e}", flush=True)

        time.sleep(1)

if __name__ == "__main__":
    main()
