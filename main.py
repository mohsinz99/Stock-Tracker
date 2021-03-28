import yfinance
import pandas
import matplotlib.pyplot


# get data on this ticker
# tickerData = yfinance.Ticker(tickersymbol)

# tickerDf = tickerData.history(period = 'id', start = '2015-1-1', end = '2020-12-31')

# print(tickerDf)

# Download data directly
# yfinance.download(tickersymbol)

class TickerSymbol:
    #download and set data
    def __init__(self):
        self.tickersymbol = 'MSFT'
        self.newtime = yfinance.download(self.tickersymbol, start = '2019-01-01', end = '2021-01-15')

# set the data
# newtime = yfinance.download(tickersymbol, start = "2014-01-01", end = "2018-12-31")

# plotting data
    def plot(self):
        self.newtime['Adj Close'].plot()
        matplotlib.pyplot.xlabel("Date")
        matplotlib.pyplot.xlabel("Adjusted Closing Price")
        matplotlib.pyplot.title(f"{self.tickersymbol} Price Data")

        matplotlib.pyplot.show()
    
    def autoUpdate(self):
        pass

ticker = TickerSymbol()

ticker.plot()