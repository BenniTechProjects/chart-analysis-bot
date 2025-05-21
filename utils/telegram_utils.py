import os
import requests

def send_telegram_message(message):
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    print("📨 Preparing to send Telegram message...", flush=True)
    print(f"🔐 Token Present: {'Yes' if bot_token else 'No'}", flush=True)
    print(f"🆔 Chat ID: {chat_id}", flush=True)

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }

    try:
        response = requests.post(url, data=data)
        print(f"📬 Telegram response: {response.status_code}, {response.text}", flush=True)
        response.raise_for_status()
    except Exception as e:
        print(f"❌ Failed to send message: {e}", flush=True)