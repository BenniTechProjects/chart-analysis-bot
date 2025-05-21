import numpy as np
import pandas as pd
import yfinance as yf

def analyze_chart(ticker):
    print(f"🔍 Running analysis for: {ticker}")

    try:
        # Download historical data (15m interval, past 5 days)
        df = yf.download(ticker, interval="15m", period="5d", progress=False)
        if df.empty:
            print(f"⚠️ No data returned for {ticker}")
            return None

        df['EMA9'] = df['Close'].ewm(span=9, adjust=False).mean()
        df['EMA20'] = df['Close'].ewm(span=20, adjust=False).mean()
        df['EMA200'] = df['Close'].ewm(span=200, adjust=False).mean()

        support = df['Close'].rolling(window=15).min().dropna().tail(3).values
        resistance = df['Close'].rolling(window=15).max().dropna().tail(3).values

        current_price = df['Close'].iloc[-1]
        signal = "CALL" if current_price > df['EMA9'].iloc[-1] and current_price > df['EMA20'].iloc[-1] else "PUT"

        target = df['Close'].rolling(window=20).mean().iloc[-1]

        return {
            "ticker": ticker,
            "support": [float(x) for x in support],
            "resistance": [float(x) for x in resistance],
            "signal": signal,
            "target": float(target)
        }

    except Exception as e:
        print(f"❌ Error analyzing {ticker}: {e}")
        return None

