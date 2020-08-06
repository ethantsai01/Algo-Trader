# Algo-Trader

A python algorithmic trader based on pre-market conditions.

A list of stocks on current news as well as companies planning to share highly anticipated earning report from that day is web scraped from various sources. This list will contain ticker symbols with a "news catalyst." Current stock information such as price and volume is web scraped off of Yahoo Finance and used to calculate volume percentage and gap percentage during pre-market times. The algorithm will make decisions to buy a stock based on the parameters set for these calculated percentages. The algorithm will continue to loop through the list of ticker symbols and will constantly buy based on these percentages until the program is terminated.
