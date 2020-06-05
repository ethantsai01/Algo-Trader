import config
from Robinhood import Robinhood

robinhood = Robinhood()
logged_in = robinhood.login(username=config.USERNAME, password=config.PASSWORD)

stock = robinhood.instruments("AAPL")[0]
print("printing stock")
print(stock)

quote = robinhood.quote_data("AAPL")
print("printing quote")
print(quote)

info = robinhood.portfolios
print("my portfolio")
print(info)