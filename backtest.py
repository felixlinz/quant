from os.path import exist as ose
import yahoocsv as ycsv
from pyalgotrade import strategy
from pyalgotrade.barfeed import yahoofeed as yf

ticker = "SPY"
timeframe = "20y"
interval = "1d"

class BTFD(strategy.BacktestingStrategy):
    def __init__(self, feed, instrument):
        super(BTFD, self).__init__(feed)
        self.instrument = instrument
        self.setUseAdjustedValues(True)
        self.position = None
        
    def onEnterOk(self, position):
        self.info(f"{position.getEntryOrder().getExecutionInfo()}")
    
    def onBars(self,bars):
        bar = bars[self.instrument]
        # self.info(bar.getClose())
        
        if self.position == None:
            close = bar.getAdjClose()
            broker = self.getBroker()
            cash = broker.getCash()
            quantity = cash/ close
            
            self.position = self.enterLong(self.instrument, quantity)
        
        
        
feed = yf.Feed()

if not (csvfile := os.path.isfile(f"~/quant/{ticker}_{timeframe}_{interval}")):
    csvfile = ycsv.getdata(ticker, timeframe, interval)
    
feed.addBarsFromCSV(ticker, csvfile)


strategy = BTFD(feed, ticker)
strategy.run()
portfolio_value = strategy.getBroker().getEquity() + strategy.getBroker().getCash()
print(portfolio_value)