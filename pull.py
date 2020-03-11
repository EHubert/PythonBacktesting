import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import sys
import random

ticker = str("AAPL")

# lines = open("keys.txt").read().splitlines()
# keys = random.choice(lines)

time = TimeSeries(key="SUMO25VBT2SJ5HQA", output_format="pandas")
data = time.get_intraday(symbol=ticker, interval="1min", outputsize="full")

# print(ticker)
# print(data)
pd.DataFrame(data[0])

print(pd)
