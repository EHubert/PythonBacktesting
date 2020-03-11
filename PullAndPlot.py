import pandas as pd
import VWAP2
import VWAP
from alpha_vantage.timeseries import TimeSeries
import backtrader as bt
import sys
import random


# Create a Stratey
class TestStrategy(bt.Strategy):
    params = (("maperiod", 15),)

    def log(self, txt, dt=None):
        """ Logging function for this strategy"""
        dt = dt or self.datas[0].datetime.date(0)
        print("%s, %s" % (dt.isoformat(), txt))

    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close
        # self.close = self.datas[0].close
        # self.volume = self.datas[0].volume
        # self.sma = bt.indicators.MovingAverageSimple(
        #    self.datas[0], period=self.params.maperiod
        # )
        self.vwap = VWAP.VolumeWeightedAveragePrice(self.datas[0])

    def next(self):
        # Simply log the closing price of the series from the reference
        self.log("Close, %.2f" % self.dataclose[0])


if __name__ == "__main__":

    # Alpha_Vantage Data capture
    ticker = str("AAPL")

    # lines = open("keys.txt").read().splitlines()
    # keys = random.choice(lines)

    time = TimeSeries(key="SUMO25VBT2SJ5HQA", output_format="pandas")
    data = time.get_intraday(symbol=ticker, interval="1min", outputsize="full")

    # print(ticker)
    # print(data)
    df = pd.DataFrame(data[0])

    cerebro = bt.Cerebro(stdstats=False)

    btdata = bt.feeds.PandasData(
        dataname=df.iloc[::-1],
        open="1. open",
        high="2. high",
        low="3. low",
        close="4. close",
        volume="5. volume",
    )

    cerebro.adddata(btdata)
    cerebro.addstrategy(TestStrategy)

    # cerebro.broker.setcash(25000.0)

    # print("Starting Portfolio Value: %.2f" % cerebro.broker.getvalue())

    cerebro.run()

    # print("FinalPortfolio Value: %.2f" % cerebro.broker.getvalue())

    cerebro.plot(
        _plotvaluetag=True,
        _name="Coolplot.jpg",
        #  Format string for the display of ticks on the x axis
        fmt_x_ticks="%Y-%b-%d %H:%M",
        # Format string for the display of data points values
        fmt_x_data="%Y-%b-%d %H:%M",
    )

