import os
import requests

def send_telegram_message(message):
    print("📨 Preparing to send Telegram message...")
    
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    
    print("🔑 Bot Token:", bot_token)
    print("🆔 Chat ID:", chat_id)

    if not bot_token or not chat_id:
        print("❌ Bot token or chat ID is missing!")
        return

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }

    try:
        response = requests.post(url, data=payload)
        print(f"🔁 Telegram response status: {response.status_code}")
        print(f"📨 Telegram response content: {response.text}")
    except Exception as e:
        print("💥 Exception occurred while sending Telegram message:", e)


