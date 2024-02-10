# sma-order-book-backtesting

I just wanted to familiarize myself with `backtesting.py` and backtest a simple moving average crossover method. Here are the results:

## Results Overview

The strategy showed varying performance over different periods. Below are the summarized results:

### Last Two Months Performance

| Metric                   | Value         |
|--------------------------|---------------|
| Return [%]               | -11.996034    |
| Buy & Hold Return [%]    | 19.725725     |
| Return (Ann.) [%]        | -47.681269    |

As evident from the table, the strategy underperformed in the last two months, indicating a significant loss compared to a buy and hold strategy.

### Performance Over the Last 5 Years

For a broader perspective, the strategy was also tested over the last 5 years of data.

| Metric                  | Value           |
|-------------------------|-----------------|
| Start                   | 2018-02-10      |
| End                     | 2024-02-10      |
| Duration                | 2191 days       |
| Exposure Time [%]       | 80.20073        |
| Equity Final [$]        | 141874.296116   |
| Equity Peak [$]         | 274367.205743   |
| Return [%]              | 1318.742961     |
| Buy & Hold Return [%]   | 191.523745      |
| Return (Ann.) [%]       | 55.528071       |
| Volatility (Ann.) [%]   | 136.811504      |
| Sharpe Ratio            | 0.405873        |
| Sortino Ratio           | 1.064793        |
| Calmar Ratio            | 0.699975        |

This comprehensive analysis over the last 5 years shows that the simple moving average crossover method significantly outperformed the buy and hold strategy, yielding a 6 times better return.

---

## Conclusion

Although the strategy's performance was quite poor in the short term, its long-term viability is evident from the 5-year backtest. It demonstrates that sometimes, simple strategies can work exceptionally well over an extended period.
