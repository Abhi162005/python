"""Module providing a function printing python version."""
import yfinance as yf
import matplotlib.pyplot as plt
TICKER_SYMBOL = "GOOGL"
google_stock = yf.Ticker(TICKER_SYMBOL)

historical_data = google_stock.history(period="6mo")
print(historical_data)
historical_data['Close'].plot(title="Google (GOOGL) Stock Price")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.show()
print()
