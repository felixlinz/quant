from backtesting import Backtest, Strategy
from backtesting.lib import crossover

from backtesting.test import SMA, SPY


class SmaCross(Strategy):
    def init(self):
        price = self.data.Close
        self.ma1 = self.I(SMA, price, 50)
        self.ma2 = self.I(SMA, price, 200)

    def next(self):
        if crossover(self.ma1, self.ma2):
            self.buy()
        elif crossover(self.ma2, self.ma1):
            self.sell()


bt = Backtest(SPY, SmaCross, commission=.002,
              exclusive_orders=True)
stats = bt.run()
bt.plot()
