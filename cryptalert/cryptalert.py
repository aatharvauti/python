from cryptocompare import get_price as gp
from webbrowser import open as op

# define prices
# get_price returns
# {'SYMBOL': {'USD': 1.000}}
# nested [foo][bar] to get value in float

# note: only use what u need, comment rest

BTC = gp('BTC', currency='USD')['BTC']['USD']
# ETH = gp('ETH', currency='USD')['ETH']['USD']
# ADA = gp('ADA', currency='USD')['ADA']['USD']
# SOL = gp('SOL', currency='USD')['SOL']['USD']
# XRP = gp('XRP', currency='USD')['XRP']['USD']
# CRO = gp('CRO', currency='USD')['CRO']['USD']
# DOT = gp('DOT', currency='USD')['DOT']['USD']
# XLM = gp('XLM', currency='USD')['XLM']['USD']
# SHIB = gp('SHIB', currency='USD')['SHIB']['USD']
# ALGO = gp('ALGO', currency='USD')['ALGO']['USD']
# NEAR = gp('NEAR', currency='USD')['NEAR']['USD']
# ATOM = gp('ATOM', currency='USD')['ATOM']['USD']
MATIC = gp('MATIC', currency='USD')['MATIC']['USD']

# simple asf code logic
# retrieve prices and compare
# if the condition satisfies, use the webbrowser module to open relevant links

if MATIC <= 1.42:
    op('https://coinmarketcap.com/currencies/polygon/')
    op('https://coindcx.com/insta/buy/matic')

if BTC >= 45000.0:
    op('https://coinmarketcap.com/currencies/bitcoin/')
    op('https://coindcx.com/insta/sell/btc')

# use this script in cronjob
# crontab -e
# * * * * * python3 /home/username/path/to/cryptalert.py
