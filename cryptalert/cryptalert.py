import json
from cryptocompare import get_price as gp

# define prices
# get_price returns
# {'SYMBOL': {'USD': 1.000}}
# nested [foo][bar] to get value in float

# note: only use what u need, comment rest

BTC = gp('BTC', currency='USD')['BTC']['USD']
ETH = gp('ETH', currency='USD')['ETH']['USD']
ADA = gp('ADA', currency='USD')['ADA']['USD']
SOL = gp('SOL', currency='USD')['SOL']['USD']
XRP = gp('XRP', currency='USD')['XRP']['USD']
CRO = gp('CRO', currency='USD')['CRO']['USD']
DOT = gp('DOT', currency='USD')['DOT']['USD']
XLM = gp('XLM', currency='USD')['XLM']['USD']
SHIB = gp('SHIB', currency='USD')['SHIB']['USD']
ALGO = gp('ALGO', currency='USD')['ALGO']['USD']
NEAR = gp('NEAR', currency='USD')['NEAR']['USD']
ATOM = gp('ATOM', currency='USD')['ATOM']['USD']
MATIC = gp('MATIC', currency='USD')['MATIC']['USD']

