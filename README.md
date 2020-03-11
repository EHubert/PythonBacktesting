# PythonBacktesting
Backtesting strategies using Backtrader and AlphaVantage

To setup your local environment: Build your local virtual environment using the requirements.txt file

PullAndPlot.py is the main file. It currently Plots AAPL in 1-min time intervals using AlphaVantage and MatPlotLib to plot.

![Imgur](https://i.imgur.com/MGkzQp9.png)

TODO:

* Fix VWAP indicator so it uses Session VWAP starting at the beginning of each day. (Currently it's using a 390 period 'Rolling VWAP')
* Add other indicators from TradingView scripts
* Consider pulling Fundamental data from a source (Rapid API, perhaps) in order to add fundamental metrics to backtesting


an additional pull.ipynb Jupyter notebook is used for as a dev scratchpad.
