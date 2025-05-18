import time
from scripts.chart_bot import run_analysis_loop

if __name__ == "__main__":
    print("✅ Chart bot starting...")
    while True:
        try:
            run_analysis_loop()  # your real function
        except Exception as e:
            print(f"❌ Error: {e}")
        time.sleep(900)  # wait 15 minutes
