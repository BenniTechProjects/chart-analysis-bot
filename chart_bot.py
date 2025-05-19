def main():
    print("🌿 Bot is running...")
    print("🤖 Telegram Bot Token:", os.getenv("TELEGRAM_BOT_TOKEN"))
    print("🆔 Telegram Chat ID:", os.getenv("TELEGRAM_CHAT_ID"))

    for ticker in WATCHLIST:
        print(f"📊 Analyzing {ticker}...")
        try:
            result = analyze_chart(ticker)
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

        except Exception as e:
            print(f"❌ Error while processing {ticker}: {e}")

        time.sleep(1)  # Delay to avoid Telegram rate limits

