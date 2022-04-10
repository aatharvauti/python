import pyqrcode
from pyqrcode import QRCode
s = "https://aatharvauti.github.io/portfolio"
url = pyqrcode.create(s)
url.png('myqr.png', scale = 6)