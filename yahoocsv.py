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

    getdata(symbol, period, interval)



def getdata(symbol, period, interval):
    try:       
        data = yf.download(f"{symbol}", period = f"{period}", interval = f"{interval}")
    except:
        raise ValueError("ivalid symbol specification")
    
    data.to_csv(f"{symbol}_{period}_{interval}.csv")
    
    return f"{symbol}_{period}_{interval}.csv"


if __name__=="__main__":
    main()