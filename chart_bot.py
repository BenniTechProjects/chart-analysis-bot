import os
import time
from utils.telegram_utils import send_telegram_message

print("✅ chart_bot.py loaded.", flush=True)

WATCHLIST = ["TEST"]

def main():
    print("🚀 Bot launched successfully.", flush=True)

    bot_token = os.getenv("TELEGRAM_BOT_TOKEN", "MISSING_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID", "MISSING_ID")
    print(f"🔑 Token: {bot_token[:10]}...", flush=True)
    print(f"🆔 Chat ID: {chat_id}", flush=True)

    send_telegram_message("🚨 TEST ALERT FROM RAILWAY BOT!")

    for ticker in WATCHLIST:
        print(f"📈 Simulating analysis for {ticker}...", flush=True)

        result = {
            "ticker": ticker,
            "support": [4.5, 4.0, 3.5],
            "resistance": [5.5, 6.0, 6.5],
            "signal": "CALL",
            "target": 5.75
        }

        print(f"✅ Mock result ready: {result}", flush=True)

        message = (
            f"*{result['ticker']}* Analysis\n"
            f"Support Levels: {result['support']}\n"
            f"Resistance Levels: {result['resistance']}\n"
            f"Signal: *{result['signal']}*\n"
            f"Target Price: {result['target']}"
        )

        print(f"📤 Sending message to Telegram:\n{message}", flush=True)
        send_telegram_message(message)
        time.sleep(1)

if __name__ == "__main__":
    print("🟣 Entering main()...", flush=True)
    main()