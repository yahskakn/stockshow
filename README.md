# stockshow
Show tabular stock data pulled from google finance

# installing prettytable:
    sudo easy_install prettytable

# installing alpha_vantage
    pip install alpha_vantage

# Running the script :
    python stockshow.py -f <filename>
    python stockshow.py -l <list of company stock codes>

    Press F1 to quit the window
# Example
    python stockshow.py -l AAPL GOOGL NFLX TSLA

![alt text](https://github.com/yahskakn/stockshow/blob/master/output.png)

# Alpha vantage
    Google seemed to be performing slow and also kicked me out of using their service as I was sending 5 requests a second. 
    So tried the ALPHA vantage API. This was worse than google in performance. I have defaulted the code to still use google finance,
    but if you want to try ALPHA Vantage change the source global var to 'ALPHA' and also get an api key from https://www.alphavantage.co/support/#api-key
    Also changing the sleep time to 1.7 seconds to see if google is okay with that refresh rate and also to abide by alpha vantage's limit of requests

# Cryptocurrencies
    Simply add BTC, ETH and/or LTC to your list of stock codes and cryptocurrency prices should show up. Pumping up the sleep time to 10s to adhere to the api 
    for this. 10 second updates is still good enough overall right?

# Snapshot
When I run the script and if I am requesting a lot of companies' stock details, I am presented with a blank screen until all that data is fetched.
Instead I now save the data fetched in previous run (the last update helps here) and refresh data once I get it.
The problem though is that the previous run could've been for a different company and if I request for a different company this time, the output is confusing.
Caching a local copy of all previously searched companies is nice, but won't scale well. What's a good solution here?
