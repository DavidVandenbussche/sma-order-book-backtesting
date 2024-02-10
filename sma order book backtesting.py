from backtesting import Backtest, Strategy
from backtesting.lib import crossover
import pandas as pd

def SMA(values, n):
    return pd.Series(values).rolling(n).mean()

class MovingAverageCrossoverStrategy(Strategy):
    n1 = 50  # Short moving average window
    n2 = 200  # Long moving average window

    def init(self):
        # Precompute the two moving averages using SMA
        self.ma1 = self.I(SMA, self.data.Close, self.n1)
        self.ma2 = self.I(SMA, self.data.Close, self.n2)

    def next(self):
        # If short MA crosses above long MA, buy
        if crossover(self.ma1, self.ma2):
            self.buy()
        # Else if short MA crosses below long MA, sell
        elif crossover(self.ma2, self.ma1):
            self.sell()

# Load Ethereum data
data = pd.read_csv('hist_data/storage_ETH-USD15m10.csv', index_col='datetime', parse_dates=True)
data.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
# data = data.interpolate()  # Handle any missing values

# print(data.head())

# Run the backtest
bt = Backtest(data, MovingAverageCrossoverStrategy, cash=10000, commission=.002)
stats = bt.run()
print(stats)
bt.plot()
