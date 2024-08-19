""" Module providing a function providing python version."""
import yfinance as yf
import matplotlib.pyplot as plt

# Fetch Google stock data (Alphabet Inc.)
stock_data = yf.Ticker('GOOGL')

# Get the last month's historical data
historical_data = stock_data.history(period="6mo")

# Plot the closing prices
plt.plot(historical_data['Close'], label='GOOGL', color='blue')
plt.title('Google Stock Price (Last Month)')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.grid(True)
plt.legend()

# Save the plot as a PNG file
plt.savefig('google_stock_price.png')

# Show the plot
plt.show()
