import yfinance as yf
import numpy as np
import pandas as pd

def analyze_chart(ticker):
    print(f"🔍 Running analysis for: {ticker}")
    try:
        data = yf.download(ticker, period="1mo", interval="1d", auto_adjust=True)
        if data.empty or len(data) < 10:
            print("🚫 Not enough data.")
            return None

        close_prices = data['Close']

        support_levels = np.round(close_prices.sort_values().head(3).tolist(), 2)
        resistance_levels = np.round(close_prices.sort_values(ascending=False).head(3).tolist(), 2)
        target = float(np.round(close_prices.mean(), 2))
        signal = "CALL" if close_prices.iloc[-1] > close_prices.mean() else "PUT"

        return {
            "ticker": ticker,
            "support": support_levels,
            "resistance": resistance_levels,
            "signal": signal,
            "target": target
        }

    except Exception as e:
        print(f"❌ Error analyzing {ticker}: {e}")
        return None
