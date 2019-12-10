import yfinance as yf
import matplotlib.pyplot as plt


##### MATPLOTLIB SECTION

apple = yf.Ticker("AAPL")
appleStock = apple.history(start='2018-01-01',end='2019-12-09')
appleOpenPrices = appleStock['Open'].tolist()
appleDates = appleStock.index.tolist()

tesla = yf.Ticker("TSLA")
teslaStock = tesla.history(start='2018-01-01',end='2019-12-09')
teslaOpenPrices = teslaStock['Open'].tolist()
teslaDates = teslaStock.index.tolist()

microsoft = yf.Ticker("MSFT")
microsoftStock = microsoft.history(start='2018-01-01',end='2019-12-09')
microsoftOpenPrices = microsoftStock['Open'].tolist()
microsoftDates = microsoftStock.index.tolist()

plt.plot(appleDates,appleOpenPrices,label='Apple')
plt.plot(teslaDates,teslaOpenPrices,label='Tesla')
plt.plot(microsoftDates,microsoftOpenPrices,label='Microsoft')
plt.legend()
plt.show()