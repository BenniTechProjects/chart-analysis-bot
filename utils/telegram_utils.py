import os
import requests

def send_telegram_message(message):
    print("📨 Preparing to send Telegram message...")
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not bot_token or not chat_id:
        print("❌ Missing bot token or chat ID!")
        return

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message, "parse_mode": "Markdown"}

    print(f"📡 Sending to URL: {url}")
    print(f"📦 Payload: {payload}")
    
    response = requests.post(url, data=payload)

    print(f"🔁 Telegram response: {response.status_code}")
    print(f"📨 Response content: {response.text}")


