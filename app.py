"""Module providing a function printing python version."""
import yfinance as yf
import matplotlib.pyplot as plt
TICKER_SYMBOL = 'AAPL'
apple_stock_data = yf.Ticker(TICKER_SYMBOL)
historical_data = apple_stock_data.history(period="1y")
print(historical_data.head())
plt.plot(historical_data.index, historical_data['Close'], label='Close Price')
plt.title('Apple (AAPL) Stock Price Over Time')
plt.xlabel('Date')
plt.ylabel('Close Price (USD)')
plt.grid(True)
plt.legend()
plt.show()
