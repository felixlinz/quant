import yfinance as yf
import sys


def main():
    if len(sys.argv) == 4:
        try:
            symbol = sys.argv[1]
            period = sys.argv[2]
            interval = sys.argv[3]
        except IndexError:
            sys.exit()
    else:
        symbol = input("symbol: ")
        period = input("period: ")
        interval = input("interval: ")

        
    data = yf.download("SPY", period = "20y", interval = "1d")

    data.to_csv(f"{symbol}_{period}_{interval}.csv")


if __name__=="__main__":
    main()