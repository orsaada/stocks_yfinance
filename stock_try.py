import yfinance as yf
import json


class Stock:

    def __init__(self, stock_symbol):
        stock_symbol = "MSFT"
        self.msft = yf.Ticker(stock_symbol)

    # get stock info
    def get_info(self):
        return self.msft.info

    # get historical market data
    def get_history(self):
        hist = self.msft.history(period="max")
        return hist

    # show actions (dividends, splits)
    def show_actions(self):
        return self.msft.actions

    # show dividends
    def show_dividends(self):
        return self.msft.dividends

    # show splits
    def show_splits(self):
        return self.msft.splits

    # show financials
    def show_financial(self):
        return self.msft.financials, self.msft.quarterly_financials

    # show major holders
    def show_major_holders(self):
        return self.msft.major_holders

    # show institutional holders
    def show_institutional_holders(self):
        return self.msft.institutional_holders

    # show balance sheet
    def show_balance_sheet(self):
        return self.msft.balance_sheet, self.msft.quarterly_balance_sheet

    # show cashflow
    def show_cashflow(self):
        return self.msft.cashflow, self.msft.quarterly_cashflow

    # show earnings
    def show_earnings(self):
        self.msft.earnings, self.msft.quarterly_earnings

    # show sustainability
    def show_sustainability(self):
        return self.msft.sustainability

    # show analysts recommendations
    def analysts_recommendations(self):
        return self.msft.recommendations

    # show next event (earnings, etc)
    def next_event(self):
        return self.msft.calendar

    # show ISIN code - *experimental*
    # ISIN = International Securities Identification Number
    def isin(self):
        return self.msft.isin

    # show options expirations
    def option(self, date):
        return self.msft.options

    # get option chain for specific expiration
    def option(self, date):
        date = date
        opt = self.msft.option_chain('YYYY-MM-DD')
        return opt
    # data available via: opt.calls, opt.puts


def to_json(data):
    import json
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    s = Stock("msft")
    print(s.get_info())
    from inspect import getmembers, isfunction
    print(getmembers(Stock, isfunction))
    # to_json(s.get_info())
