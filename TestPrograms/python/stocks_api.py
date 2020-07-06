import requests
import json
def stockprice(symbol):
    r = requests.get('https://finnhub.io/api/v1/quote?symbol=' + symbol + '&token=bqrl2qnrh5resd1bp5sg&')
    return r.json()
input = input("Type in the symbol of the stock price you want to know? ")
input = input.upper()
stockprice = stockprice(input)
print('Closing Price of ' + input + ' is $' + str(stockprice['c']))
