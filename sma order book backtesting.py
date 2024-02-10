import pandas as pd
from backtesting import Backtest, Strategy
from backtesting.lib import crossover

def calculate_sma(prices, window):
    return prices.rolling(window).mean()

class SMAStrategy(Strategy):
    def init(self):
        self.sma20 = self.I(calculate_sma, self.data.Close, 20)

    def next(self):
        # If current price crosses over SMA from below, and not already long, buy
        if not self.position.is_long and self.data.Close[-1] > self.sma20[-1]:
            self.buy()

        # If current price crosses under SMA from above, and not already short, sell
        elif not self.position.is_short and self.data.Close[-1] < self.sma20[-1]:
            self.sell()

# Load Ethereum data past 10 weeks freq of 15m
data = pd.read_csv('hist_data/storage_ETH-USD15m10.csv', index_col='datetime', parse_dates=True)
data.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
# data = data.interpolate()  # Handle any missing values

bt = Backtest(data, SMAStrategy, cash=10_000, commission=.002)
output = bt.run()
print(output)
bt.plot()
