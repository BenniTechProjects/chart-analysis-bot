import os
import requests

def send_telegram_message(message):
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    print("📨 Preparing to send Telegram message...")
    print(f"🔑 Token: {bot_token}")
    print(f"🆔 Chat ID: {chat_id}")

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }

    try:
        response = requests.post(url, data=data)
        print(f"📬 Telegram response: {response.status_code}, {response.text}")
        response.raise_for_status()
    except Exception as e:
        print(f"❌ Failed to send message: {e}")