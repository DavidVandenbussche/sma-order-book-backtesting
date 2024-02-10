# sma-order-book-backtesting

So I just wanted to familiarize myself with backtsting.py and backtest a simple moving average crossover method, the results are as follow:

Return [%]                         -11.996034
Buy & Hold Return [%]               19.725725
Return (Ann.) [%]                  -47.681269


meaning pretty bad obviously on the last two months, however it is interesting to note that if this strategy had been launched on the full 5 past years of data then the results are:

Start                     2018-02-10 00:00:00
End                       2024-02-10 00:00:00
Duration                   2191 days 00:00:00
Exposure Time [%]                    80.20073
Equity Final [$]                141874.296116
Equity Peak [$]                 274367.205743
Return [%]                        1318.742961
Buy & Hold Return [%]              191.523745
Return (Ann.) [%]                   55.528071
Volatility (Ann.) [%]              136.811504
Sharpe Ratio                         0.405873
Sortino Ratio                        1.064793
Calmar Ratio                         0.699975

with a 6 times better return than just holding. Sometimes simple work!
